# syntax
## value 
无法继续步进简化的表达式
## if expression
if e1 then e2:t2 else e3:t2
分支的类型必须相同，e1的类型为布尔，则表达式的类型为t2

## definition(let expression)
bind a value to a name 
```
let x =e
```
1. evaluate e to a value v
2. bind v to x ,henceforth x will evaluate to v
3. definition has no value,so can  not be in a expression
```
let b =1 in 2* b;;
```
in 关键字连接定义和表达式

## function 
1. 函数是一个具体的值
2. 函数体在调用后才会开始计算


# semantics
1. 静态类型检查
2. 取值，触发异常或者无限循环
# idioms (common patterns)
# libraries(extension)
# tools(top-level,debugger,Gui editor)

