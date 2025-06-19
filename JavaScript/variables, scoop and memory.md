# 原始值和引用值
primitive value and reference value
## by value versus by refernce
## dynamic properties
by reference,can add ,change and delete operation
## copy value
![alt text](JavaScript/image-3.png)
## argument passing 
shallow copy the value to the argument
the instanceof operator
```javascript
result=varialbe instanceof contrucor
```
# context and scoop
## the scope chain 
from child to father 
```javascript
var color = "blue"
function changeColor(){
	if (color==="bule"){
		color="red";
	}else{
		color="blue";
	}
}
// function scope chain : activation object and global 
```
![alt text](JavaScript/image-4.png)
## boost the scoope chain
### try/catch 
add a variable object at rhe front of scoop chain
### with 
the variable declared by var will be part of the father context
## variable declaration
### var
1. the variable will be added to the closest context,without the keyword it will be added to the global context
### let
the scoope of let variable is in the block.aka {}
### const
declaration with the initialization and can not be assigned with new value
### identifier lookup
```javascript
var color = 'blue';
function getColor() {
let color = 'red';
{
	let color = 'green';
	return color;
}
}
console.log(getColor()); // 'green'
```
## garbage collection
### mark and sweep
垃圾回收程序运行的时候，会标记内存中存储的所有变量（记住，标记方法有很多种）。然后，它会将所有在上下文中的变量，以及被在上下文中的变量引用的变量的标记去掉。
### reference counting
```javascript
function problem() {
let objectA = new Object();
let objectB = new Object();
objectA.someOtherObject = objectB;
objectB.anotherObject = objectA;
}
```
### performace
1. JavaScript 引擎的垃圾回收程序被调优为动态改变分配变量、字面量或数组槽位等会触发垃圾回收的阈值
2. 解除引用的关键在于确保相关的值已经不在上下文里了，因此它在下次垃圾回收时会被回收。
