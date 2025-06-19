## bitwise operations

| 中文  | sign |
| --- | ---- |
| 与   | &    |
| 或   | \|   |
| 异或  | ^    |
| 反   | ~    |
| 左移  | <<   |
| 右移  | >>   |

[[bitshift.c|example code]]
[[packed_data|packed_data示意图]]
## preprocessor(预处理)
### define 
==1. 一个预定义的名字不能看作变量，可以理解为后续程序中所有同名的位置都会被定义取代==
==2.建议使用大写用于区别普通函数==
==3.定义可以用于运算符==
==4.可以构建不限定参数的宏以提高可读性==
5.用...定义未确定的参数同时后续通过\_VA_ARGS_ __

[[evenodd.c|奇偶数检测]]
```
#define square(x)  ((x)*(x))  
#define is_lower_case(x)  (((x)>='a') && ((x)<='z'))
#define to_upper(x) (is_lower_case(x) ? (x)-'a'+'A': (x))
#define debugPrintf(...) printf ("DEBUG:" _ _VA_ARGS_ _);

#define str(x) # x
#define printx(n) printf ("%i\n", x ## n)
```

### include
预读取其他文件，类似于python的import 
```
include<stdio.h>
```

### conditional compliation 
```
#ifdef UNIX
# define DATADIR "/uxn1/data"
#else
# define DATADIR "\usr\data"
#endif
```
可以预读取命令行的参数输入
> [!example]
> gcc -D GNUDIR=/c/gnustep program.c

## enumerate date type
1. 允许其中元素的初始化赋值
2. 通过cast的方式进行枚举类型数据的值
```
monthvalue=6;
thismonth= (enum month) (monthvalue -1);
```

### typedef
构建新的数据类型
```
typedef char linebuf [81];
typedef char *stringptr;
```

[[My code file.c|sample code]]
### 类型转化的规则
1. 其中一个类型是long double/double/float/long long int,运算结果转化为long double/double/float/long long int
2. \_bool,char,short int ,bit field, 转化为int
## working with larger programs
### 分割大项目成多个小项目
```
static int movenumber =0 
static double squareroot(double x)
// 如果定义在任何函数之外，则该变量仅能被本文件的读取
```

## miscellaneous and advanced features
```
union mixed
{
    char c;
     float f;
     int i;
}
```

union与struct的区别在于两者的对待内存的方式不同，前者只能选择其包含元素中的一个

### type qualifiers
1. register 常用寄存数据
2. volatile 避免编译器对程序的优化，表明该变量一定会发生变化
3. restrict 表明指针指定对象不可更改，两个restrict指针不能指向同一个对象
### 命令行参数
argc 参数数量
argv包含字符指针的array
![[arguments]]
### dynamic memory allocation
1. calloc() 需保存元素的数目 每个元素所需内存大小 内存自动设置为0
2. malloc()  所需的总内存大小 总内存设置为0
3. sizeof()返回对象所需的字节数目
[[addentry.c|添加链接列表元素]]
## debug
```
gcc –D DEBUG debug.c
等同于添加#define debug 
```