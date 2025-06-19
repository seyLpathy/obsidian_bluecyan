# String class
## constructor
[[string1.cpp|different constructors]]

## input
```cpp
char info[100];
cin >> info; // read a word
cin.getline(info, 100); // read a line, discard \n
cin.get(info, 100); // read a line, leave \n in queue
---
//string stuff;
cin >> stuff; // read a word
getline(cin, stuff); // read a line, discard \n

//geline()
cin.getline(info,100,':'); // read up to :, discard :
getline(stuff, ':'); // read up to :, discard :
```

### getline读取终止条件
1.  endoffile ,eofbit is set,and ==fail()/eof() return True==
2.  delimiting character reached,default is \n
3. maximum possible number of character(==string::npos和剩余内存字节数的较小者==)

## 使用string
### operator overload
```cpp
string snake1("cobra");
string snake2("coral");
char snake3[20] = "anaconda";
if (snake1 < snake 2) // operator<(const string &, const string &)
...
if (snake1 == snake3) // operator==(const string &, const char *)
...
if (snake3 != snake2) // operator!=(const char *, const string &)
...
```

### 字符长度
. size()
. length()

### search

| method prototype                                                  | description                                                                                                                                             |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| size_type find(const string &<br>str, size_type pos = 0) const    | Finds the first occurrence of the substring str,<br>starting the search at location pos in the invoking string.                                         |
| size_type find(const char * s,<br>size_type pos = 0) const        | Finds the first occurrence of the substring s,<br>starting the search at location pos in the invoking string                                            |
| size_type find(const char * s,<br>size_type pos = 0, size_type n) | Finds the first occurrence of the substring<br>consisting of the first n characters in s, starting<br>the search at location pos in the invoking string |
| size_type find(char ch, size_type<br>pos = 0) const               | Finds the first occurrence of the character ch,<br>starting the search at location pos in the invoking string.                                          |
## 补充
```cpp
template<class charT, class traits = char _traits<charT>,
class Allocator = allocator<charT> >
basic_string {...};
```

# smart pointer智能指针
## utillity
**class unique_ptr,shared_ptr**
```cpp
unique_ptr<double> pdu(new double); // pdu an unique_ptr to double
shared_ptr<string> pss(new string); // pss a shared_ptr to string
```
### steps
1. Include the memory header file.
2. Replace the pointer-to-string with a smart pointer object that points to string.
3. Remove the delete statement.
```cpp
shared_ptr<double> pd;
double *p_reg = new double;
pd = p_reg; // not allowed (implicit conversion)
pd = shared_ptr<double>(p_reg); // allowed (explicit conversion
shared_ptr<double> pshared = p_reg; // not allowed (implicit conversion)
shared_ptr<double> pshared(p_reg); // allowed (explicit conversion)
```
### exceptions
1. delete operator to non-heap memory
```	
string vacation("I wandered lonely as a cloud.");
shared_ptr<string> pvac(&vacation); // NO!
```

### key points 
1. shared_ptr 可以和普通的指针指向同一个对象
2. the unique_ptr version yields a compiletime error objecting to this line:
```cpp
auto_ptr<string> films[5] =
{
shared_ptr<string> (new string("Fowl Balls")),
shared_ptr<string> (new string("Duck Walks")),
shared_ptr<string> (new string("Chicken Runs")),
shared_ptr<string> (new string("Turkey Errors")),
shared_ptr<string> (new string("Goose Eggs"))
};
shared_ptr<string> pwin;
pwin = films[2]; // films[2] loses ownership
```

# vector class
## 使用vector
### declare an iterator for vector
```cpp
vector<double>::iterator pd;
vector<double> scores;
pd = scores.begin(); // have pd point to the first element
*pd=22.3; // assign value to first element 
++pd,//make pd point to the next element_

auto pd = scores.begin();

// iterate the whole content  of container
for (pd = scores.begin(); pd != scores.end(); pd++)
    cout << *pd << endl;;

```

### 实用的方法
1. push_back() add an element to the end of a vector
2. erase(two iterator arguments )  [p1,p2)]
![[Drawing 2024-06-04 22.43.29.excalidraw]]

3. insert()
```
old_v.insert(old_v.begin(), new_v.begin() + 1, new_v.end());
```

### nonmember function 
```
for_each(books.begin(), books.end(), ShowReview); 
random_shuffle(books.begin(), books.end());
vector<int> coolstuff;
...
sort(coolstuff.begin(), coolstuff.end());
```
#### sort
sort(books.begin(), books.end(), function);
bool function 
#### for loop
```
double prices[5] = {4.99, 10.99, 6.87, 7.99, 8.49};
for (double x : prices)
cout << x << std::endl;

for_each(books.begin(), books.end(), ShowReview);
for (auto x : books) ShowReview(x);
```

# generic programming
## kinds of iterator
### input iterators
1. read values from a container but not allowed to alter the values
2. support the ++ operator
3. no garantee that the traversing will always move through in the same order
4. can increment,but it can't back up
###  output iterators
1. alter a container value but not to read 
2. for single-pass ,write only algorithms
### forward iterator
1. only go forward through a container one element
2. go through a sequence of values in the same order
3. can dereference the prior iterator value
```
int * pirw; // read-write iterator
const int * pir; // read-only iterator
```

### bidirectional iterators
1.  possess all the feature of a forward iterator and adds
2. support for the two decrement operator
### random access iterators
1. all the features of a bidirectional iterator,
2. adds operations (such as pointer addition) that support random access and relational operators for ordering the elements

## iterator hierarchy
![[Pasted image 20240605190115.png]]
# functor

^3b63ef

## concept
1. A generator is a functor that can be called with no arguments.
2. A unary function is a functor that can be called with one argument.
3. A binary function is a functor that can be called with two arguments.
```cpp
class Linear
{
	private:
	double slope;
	double y0;
	public:
	Linear(double sl_ = 1, double y_ = 0)
	: slope(sl_), y0(y_) {}
	double operator()(double x) {return y0 + slope * x; }
};
```

