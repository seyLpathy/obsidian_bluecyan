# basics

1. case sensitive
2. 标识名，使用驼峰大小写形式
3. comment //
4. "use strict"
5. sentence end with colon
6. keywords
   ![alt text](JavaScript/image-1.png)
7. variables
   1. var 使用 var 操作符定义的变量会成为包含它的函数的局部变量,关键字声明的变量会自动提升到函数作用域顶部
   ```
   	function test(){
   		var message="hi"; //local variables
   		// message="hi" global variables
   	}
   	test();
   	console.log(message);
   ```
   2. let 声明的变量只在 let 命令所在的代码块内有效,也不允许同一个块作用域中出现冗余声明
   3. global declaration
   ```
   var name='Matt';
   console.log(window.name);
   let age=26;
   console.log(window.age); // undifined
   ```
   4. let keywords in for loop
   5. const声明变量时必须同时初始化变量，且尝试修改const 声明的变量会导致运行时错误。只适用于它指向的变量的引用
# data type
## types
### undifined
当使用var 或let 声明了变量但没有初始化时，就相当于给变量赋予了undefined 值
==无论是声明还是未声明，typeof 返回的都是字符串"undefined"。==
### null
null 值表示一个空对象指针
```
let car = null;
console.log(typeof car); // "object"
```
### boolean
![alt text](JavaScript/image-2.png)

### number
```javascript
let intNum = 55; // 整数
let octalNum1 = 070; // 八进制的56
let octalNum2 = 079; // 无效的八进制值，当成79 处理
let octalNum3 = 08; // 无效的八进制值，当成8 处理
let hexNum1 = 0xA; // 十六进制10
let hexNum2 = 0x1f; // 十六进制31
```
#### 浮点数
在小数点后面没有数字的情况下，数值就会变成整数。
#### range of number
Number.MIN_VALUE/Number.MAX_VALUE
isFinite()函数
#### NaN
isNaN()函数
不是数值”（Not a Number），用于表示本来要返回数值的操作失败了（而不是抛出错误）。

#### transform
Number()、parseInt()和parseFloat()。Number()是转型函数，可用于任何数据类型。后两个函数主要用于将字符串转换为数值。
```javascript
let num1 = parseInt("AF", 16); // 175
```
### string
要修改某个变量中的字符串值，必须先销毁原始的字符串，然后将包含新值的另一个字符串保存到该变量
toString()方法
#### 插值
```javascript
let value = 5;
let result = `the value is ${value}`;
```
### symbol
1. 符号需要使用Symbol()函数初始化。因为符号本身是原始类型，所以typeof 操作符对符号返回symbol。
2. 最重要的是，Symbol()函数不能与new 关键字一起作为构造函数使用。
```
let fooGlobalSymbol = Symbol.for('foo'); // 创建新符号
let otherFooGlobalSymbol = Symbol.for('foo'); // 重用已有符号
console.log(fooGlobalSymbol === otherFooGlobalSymbol); // true
```
还可以使用Symbol.keyFor()来查询全局注册表，这个方法接收符号，返回该全局符号对应的字
符串键。如果查询的不是全局符号，则返回undefined。
### object
1. constructor
2. hasownproperty
3. isprototypeof
5. propertyIsEnumerable
6. toLocaleString
7. toString
8. valueOf
## typeof operator
```
let message = "some string";
console.log(typeof message); // "string"
console.log(typeof(message)); // "string"
console.log(typeof 95); // "number"
```
