---
tags:
  - make
  - program
---
# GNUmake

## makefile syntax

```makefile
targets: prerequisites  # target指代文件名或者标签，一个或者多个
command                 # prerequisites指代前置条件，一般是编译后的文件
command                 # command指代运行具体的命令
command
```

## essence of Make

1. makefile中第一个目标为默认目标
2. target是否能够运行取决于prerequisite的文件是否新于target(假定prerequisite存在的话），或者target同名的文件不存在
3. 运作标志在于文件系统的时间戳进行运行判定

### example

```makefile
blah: blah.o
	cc blah.o -o blah # Runs third

blah.o: blah.c
	cc -c blah.c -o blah.o # Runs second

# Typically blah.c would already exist, but I want to limit any additional required files
blah.c:
	echo "int main() { return 0; }" > blah.c # Runs first
```

### make clean(主要用于移除输出文件）

```makefile
some_file: 
	touch some_file

clean:
	rm -f some_file
```

## variables

1. 单引或者双引没有意义，只是单纯的字符
2. 使用`:=进行赋值`

```makefile
files := file1 file2
some_file: $(files)
	echo "Look at this variable: " $(files)
	touch some_file
file1:
	touch file1
file2:
	touch file2
clean:
	rm -f file1 file2 some_file
```

### import rules
1. 用`${}` or `$()来引用变量的值`
2. 用 = 进行赋值时，“:=”右边的表达式如果包含对变量的引用，则这些对变量的引用会直接展开，得到一个确切的值，并赋给“:=”左边的变量。
3. 在使用“=”定义变量时，如果“=”右边存在对其他变量或函数的引用，这些引用并不会立即展开。在实际使用到递归展开变量时，递归展开变量才会展开，同时定义递归展开变量时使用的其他变量或函数的引用也会被展开，从而得到当前递归展开变量的值。在引用递归展开变量的地方，执行的是严格的文本替换过程，递归展开变量中的字符串原模原样的出现在引用变量的地方，而递归展开变量中对其他变量的引用，只会在递归展开变量被展开的同时被展开。
4. ?=仅适用于未被定义的变量
5. 使用$(nullstring)表示空格 ，同时未被定义的变量也为空字符串
6. +=进行文本后缀添加
7. 使用 覆盖函数对make命令的参数进行覆盖
8. ；进行shell分割而/表示处于同一shell
9. 可以针对特定的target进行变量赋值

```makefile
# Overrides command line arguments
override option_one = did_override
# Does not override command line arguments
option_two = not_override
all: 
	echo $(option_one)
	echo $(option_two)
all: one = cool
all: 
	echo one is defined: $(one)
other:
	echo one is nothing: $(one)
```

## targets

1. all 同时触发所有的目标
2. 同一规则下多个目标，命令会对每一个目标进行调用
3. $@表示当前目标名

```makefile
all: one two three
one:
	touch one
two:
	touch two
three:
	touch three
clean:
	rm -f one two three

```

```makefile
all: f1.o f2.o
f1.o f2.o:
	echo $@
# Equivalent to:
# f1.o:
#	 echo f1.o
# f2.o:
#	 echo f2.o
```

## wildcard

### * wildcard

```makefile
print: $(wildcard *.c) #*一般用于文件，在无条件符合的情况下，既保留文本含义
	ls -la  $?
```

```makefile
thing_wrong := *.o # Don't do this! '*' will not get expanded
thing_right := $(wildcard *.o)
all: one two three four
# Fails, because $(thing_wrong) is the string "*.o"
one: $(thing_wrong)
# Stays as *.o if there are no files that match this pattern :(
two: *.o 
# Works as you would expect! In this case, it does nothing.
three: $(thing_right)
# Same as rule three
four: $(wildcard *.o)
```

### % wildcard

1. 在匹配模式下，可能匹配多个字符，称为stem
2. 在替代模式下，需要stem存在并进行调换
3. % 多用于规则定义和特定函数

## 自动变量

```makefile
hey: one two
	# Outputs "hey", since this is the target name
	echo $@
	# Outputs all prerequisites newer than the target
	echo $?
	# Outputs all prerequisites
	echo $^
	touch hey
one:
	touch one
two:
	touch two
clean:
	rm -f hey one two
```

## 隐性规则

```makefile
CC = gcc # Flag for implicit rules
CFLAGS = -g # Flag for implicit rules. Turn on debug info

# Implicit rule #1: blah is built via the C linker implicit rule
# Implicit rule #2: blah.o is built via the C compilation implicit rule, because blah.c exists
blah: blah.o

blah.c:
	echo "int main() { return 0; }" > blah.c

clean:
	rm -f blah*
```

## 静态模式规则

```makefile
objects = foo.o bar.o all.o
all: $(objects)
# These files compile via implicit rules
# Syntax - targets ...: target-pattern: prereq-patterns ...
# In the case of the first target, foo.o, the target-pattern matches foo.o and sets the "stem" to be "foo".
# It then replaces the '%' in prereq-patterns with that stem
$(objects): %.o: %.c
all.c:
	echo "int main() { return 0; }" > all.c
%.c:
	touch $@
clean:
	rm -f *.c *.o all

```

## 模式规则

```makefile
%.o : %.c
		$(CC) -c $(CFLAGS) $(CPPFLAGS) $< -o $@
# Define a pattern rule that has no pattern in the prerequisites.
# This just creates empty .c files when needed.
%.c:
   touch $@
```

## 双冒号规则

```makefile
all: blah
blah::
	echo "hello"
blah::
	echo "hello again"
```

## 命令和执行

1. 在命令行前加入@可以使命令避开打印
2. 每一条命令在不同的框架下运行
3. 默认shell是/bin/sh，SHELL变量可以进行调换
4. $$表示$符号
5. -k 在遇到错误的情况下，继续进行运行makefile.-i可以屏蔽所有命令的错误，-置于某一个命令前可以屏蔽某一条命令

## 修整和特点

1. make的回调使用($MAKE)
2. EXPORT 将变量转变为环境变量

```makefile
.EXPORT_ALL_VARIABLES:
new_contents = "hello:\n\techo \$$(cooly)"
cooly = "The subdirectory can see me!"
# This would nullify the line above: unexport cooly
all:
	mkdir -p subdir
	printf $(new_contents) | sed -e 's/^ //' > subdir/makefile
	@echo "---MAKEFILE CONTENTS---"
	@cd subdir && cat makefile
	@echo "---END MAKEFILE CONTENTS---"
	cd subdir && $(MAKE)

clean:
	rm -rf subdir
```

## 条件设定

1. if/else

```makefile
foo = ok
all:
ifeq ($(foo), ok)
	echo "foo equals ok"
else
	echo "nope"
endif
```

1. 判断变量是否为空

```makefile
nullstring =
foo = $(nullstring) # end of line; there is a space here
all:
ifeq ($(strip $(foo)),)
	echo "foo is empty after being stripped"
endif
ifeq ($(nullstring),)
	echo "nullstring doesn't even have spaces"
endif
```

1. 判断变量是否定义

```makefile
bar =
foo = $(bar)

all:
ifdef foo
	echo "foo is defined"
endif
ifndef bar
	echo "but bar is not"
endif
```

1. 判断是否make命令调用特定flag

```makefile
all:
# Search for the "-i" flag. MAKEFLAGS is just a list of single characters, one per flag. So look for "i" in this case.
ifneq (,$(findstring i, $(MAKEFLAGS)))
	echo "i was passed to MAKEFLAGS"
endif
```

## 函数

1. 常用内置函数(patsubst)文本替代

```makefile
comma := ,
empty:=
space := $(empty) $(empty)
foo := a b c
bar := $(subst $(space),$(comma),$(foo))

all: 
	@echo $(bar)
```

1. foreach函数

```makefile
foo := who are you
# For each "word" in foo, output that same word with an exclamation after
bar := $(foreach wrd,$(foo),$(wrd)!)
all:
	# Output is "who! are! you!"
	@echo $(bar)
```

1. if函数

```makefile
foo := $(if this-is-not-empty,then!,else!)
empty :=
bar := $(if $(empty),then!,else!)

all:
	@echo $(foo)
	@echo $(bar)
```

1. call函数(主要用于构建自定义函数）

```makefile
sweet_new_fn = Variable Name: $(0) First: $(1) Second: $(2) Empty Variable: $(3)

all:
	# Outputs "Variable Name: sweet_new_fn First: go Second: tigers Empty Variable:"
	@echo $(call sweet_new_fn, go, tigers)
```

1. vpath指令（路径搜索）

```makefile
vpath %.h ../headers ../other-directory
# Note: vpath allows blah.h to be found even though blah.h is never in the current directory
some_binary: ../headers blah.h
	touch some_binary
../headers:
	mkdir ../headers

# We call the target blah.h instead of ../headers/blah.h, because that's the prereq that some_binary is looking for
# Typically, blah.h would already exist and you wouldn't need this.
blah.h:
	touch ../headers/blah.h

clean:
	rm -rf ../headers
	rm -f some_binary
```

1. 使用backslash将长命令分割为多行
2. .phony用于屏蔽target同名文件的存在对make的影响
3. **.delete_on_error在命令返回一个非零状态的情况下，中断命令**

## example

```makefile
# Thanks to Job Vranish (https://spin.atomicobject.com/2016/08/26/makefile-c-projects/)
TARGET_EXEC := final_program

BUILD_DIR := ./build
SRC_DIRS := ./src

# Find all the C and C++ files we want to compile
# Note the single quotes around the * expressions. The shell will incorrectly expand these otherwise, but we want to send the * directly to the find command.
SRCS := $(shell find $(SRC_DIRS) -name '*.cpp' -or -name '*.c' -or -name '*.s')

# Prepends BUILD_DIR and appends .o to every src file
# As an example, ./your_dir/hello.cpp turns into ./build/./your_dir/hello.cpp.o
OBJS := $(SRCS:%=$(BUILD_DIR)/%.o)

# String substitution (suffix version without %).
# As an example, ./build/hello.cpp.o turns into ./build/hello.cpp.d
DEPS := $(OBJS:.o=.d)

# Every folder in ./src will need to be passed to GCC so that it can find header files
INC_DIRS := $(shell find $(SRC_DIRS) -type d)
# Add a prefix to INC_DIRS. So moduleA would become -ImoduleA. GCC understands this -I flag
INC_FLAGS := $(addprefix -I,$(INC_DIRS))

# The -MMD and -MP flags together generate Makefiles for us!
# These files will have .d instead of .o as the output.
CPPFLAGS := $(INC_FLAGS) -MMD -MP

# The final build step.
$(BUILD_DIR)/$(TARGET_EXEC): $(OBJS)
	$(CXX) $(OBJS) -o $@ $(LDFLAGS)

# Build step for C source
$(BUILD_DIR)/%.c.o: %.c
	mkdir -p $(dir $@)
	$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@

# Build step for C++ source
$(BUILD_DIR)/%.cpp.o: %.cpp
	mkdir -p $(dir $@)
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) -c $< -o $@

.PHONY: clean
clean:
	rm -r $(BUILD_DIR)
