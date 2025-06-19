# date
## constructor
```javascript
let someDate = new Date(Date.parse("May 23, 2019"));
let someDate = new Date("May 23, 2019");
// GMT 时间2000 年1 月1 日零点
let y2k = new Date(Date.UTC(2000, 0));
// GMT 时间2005 年5 月5 日下午5 点55 分55 秒
let allFives = new Date(Date.UTC(2005, 4, 5, 17, 55, 55));
```
## inheritance methods
1. tolocaleString() 方法返回与浏览器运行的本地环境一致的日期和时间
2. toString() 通常返回带时区信息的日期和时间，而时间也是以24 小时制（0~23）表示的
3. valueof() Date 类型的valueOf()方法根本就不返回字符串，这个方法被重写后返回的是日期的毫秒表示。因此，操作符（如小于号和大于号）可以直接使用它返回的值。
```javascript
let date1 = new Date(2019, 0, 1); // 2019 年1 月1 日
let date2 = new Date(2019, 1, 1); // 2019 年2 月1 日
console.log(date1 < date2); // true
console.log(date1 > date2); // false
```
## regExp
```javascript
let text = "mom and dad and baby";
let pattern = /mom( and dad( and baby)?)?/gi;
let matches = pattern.exec(text);
console.log(matches.index); // 0
console.log(matches.input); // "mom and dad and baby"
console.log(matches[0]); // "mom and dad and baby"
console.log(matches[1]); // " and dad and baby"
console.log(matches[2]); // " and baby"
let pattern2 = new RegExp("[bc]at", "i");
```
exec返回的数组Array 的实例，但包含两个额外的属性：index 和input。index 是字符串中匹配模式的起始位置，input 是要查找的字符串.
```javascript
let text = "mom and dad and baby";
let pattern = /mom( and dad( and baby)?)?/gi;
let matches = pattern.exec(text);
console.log(matches.index); // 0
console.log(matches.input); // "mom and dad and baby"
console.log(matches[0]); // "mom and dad and baby"
console.log(matches[1]); // " and dad and baby"
console.log(matches[2]); // " and baby
```
>[!summary]
>正则表达式的另一个方法是test()，接收一个字符串参数。如果输入的文本与模式匹配，则参数返回true，否则返回false。

toLocaleString()和toString()返回的都是其字面量的形式。
![alt text](JavaScript/image-5.png)
## premitive wrapper types
```javascript
let s1 = "some text";
let s2 = new String("some text");
```
(1) 创建一个String 类型的实例
(2) 调用实例上的特定方法；
(3) 销毁实例
### boolean
```javascript
let booleanObject = new Boolean(true);
let falseObject = new Boolean(false);
let falseValue = false;
console.log(typeof falseObject); // object
console.log(typeof falseValue); // boolean
console.log(falseObject instanceof Boolean); // true
console.log(falseValue instanceof Boolean); // false
```