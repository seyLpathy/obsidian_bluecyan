# friends,exceptions,and more
## friends
>[!definition]
>一个friend类的方法能够访问主类的private和public members
### friend class
其成员方法需要对应到特定的主类对象，所以对应的参数类型为主类的refrence
```c++
public:
friend class Remote; // Remote can access Tv private parts
enum {Off, On};
```

```c++
Remote(int m = Tv::TV) : mode(m) {}
bool volup(Tv & t) { return t.volup();}
void set_chan(Tv & t, int c) {t.channel = c;}
```
### friend member functions
```c++
class Tv;  //forward declaration
class Remote{. . .};
class Tv
{
friend void Remote::set_chan(Tv & t, int c);// friend member function
...
};
```

### shared friends 
a function to both classes
```c++
class Probe
{
	friend void sync(Analyzer & a, const Probe & p); // sync a to p
	friend void sync(Probe & p, const Analyzer & a); // sync p to a
...
};
class Analyzer
{
friend void sync(Analyzer & a, const Probe & p); // sync a to p
friend void sync(Probe & p, const Analyzer & a); // sync p to a
...
};
// define the friend functions
inline void sync(Analyzer & a, const Probe & p)
{
...
}
inline void sync(Probe & p, const Analyzer & a)
{
...
}

```
## Nested class 
一个在其他的类中申明的类称为nested class
```c++
class Queue
{
	class Node
	{
	public:
		Item item;
		Node * next;
		Node(const Item & i) : item(i), next(0) { }
	// class scope definitions
	// Node is a nested class definition local to this class
	};
	...
};
```

```c++
bool Queue::enqueue(const Item & item)
{
	if (isfull())
		return false;
	Node * add = new Node(item); 
// create, initialize node
// on failure, new throws std::bad_alloc exception
...
}
```
### nested class and access
#### scope
1. 如果定义于private部分，则只能被所定义环境的类所访问，其子类也不可访问
2. 如果定义于public部分，则能对子类及外部世界，但使用时需要加上class qualifer
#### summary
Table 15.1 Scope Properties for Nested Classes, Structures, and Enumerations

| delcaration area | access to nesting class | acess to class derived | access to outside world       |
| ---------------- | ----------------------- | ---------------------- | ----------------------------- |
| private          | yes                     | no                     | no                            |
| protect          | yes                     | yes                    | no                            |
| public           | yes                     | yes                    | yes ,but with class qualifier |
### 访问控制
nesting class 只能访问nested class 的public part 
### nesting in a template
```c++
QueueTp<double> dq;
QueueTp<char> cq;
//These two Node classes are defined in two separate QueueTP classes
```
## Exceptions
### calling abort()
>[!definition]
>abort() prototype in the cstdlib(stdlib.h)
>直接中断程序而不是返回至main()

```c++
double hmean(double a, double b)
{
	if (a == -b)
	{
		std::cout << "untenable arguments to hmean()\n";
		std::abort();
	}
	return 2.0 * a * b / (a + b);
}
```
### 返回错误代码
==you can use a pointer argument or a reference argument to get a value back
to the calling program and use the function return value to indicate success or failure==
### exception mechanism
1. 抛出异常
2. handler 捕捉异常
3. 使用try 块
```c++
try { // start of try block
	z = hmean(x,y);
} // end of try block
catch (const char * s) // start of exception handler
{
	std::cout << s << std::endl;
	std::cout << "Enter a new pair of numbers: ";
	continue;
} 
// end of handler

double hmean(double a, double b)
{
	if (a == -b)
		throw "bad hmean() arguments: a = -b not allowed";
	return 2.0 * a * b / (a + b);
}
```

[[excpetion mechanism|scheme]]
### exception objects
```c++
try { // start of try block
...
}// end of try block
catch (bad_hmean & bg) // start of catch block
{
...
}
catch (bad_gmean & hg)
{
...
} // end of catch block
```
### unwinding the stack
>[!question]
>a try block doesn’t contain a direct call to a function that throws an exception
>but that it calls a function that calls a function that throws an exception