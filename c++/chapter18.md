# feature
## uniform initialization
```cpp
int x = {5};
double y {2.75};
short quar[5] {4,5,2,76,1};
class Stump
{
private:
int roots;
double weight;
public:
Stump(int r, double w) : roots(r), weight(w) {}
};
Stump s1(3,15.6); // old style
Stump s2{5, 43.4}; // C++11
Stump s3 = {4, 32.1}; // C++11
```

## narrow
```cpp
char c1 {1.57e27}; // double-to-char, compile-time error
char c2 = {459585821};// int-to-char,out of range, compile-time error
char c1 {66}; // int-to-char, in range, allowed
double c2 = {66}; // int-to-double, allowed
```

## Declaration
### auto
```cpp
auto maton = 112; // maton is type int
auto pt = &maton; // pt is type int *
double fm(double, int);
auto pf = fm; // pf is type double (*)(double,int)
```

### decltype
```cpp
double x;
int n;
decltype(x*n) q; // q same type as x*n, i.e., double
decltype(&x) pd; // pd same as &x, i.e., double *
```

## trailing
```cpp
double f1(double, int); // traditional syntax
auto f2(double, int) -> double; // new syntax, return type is double
```

## template alaises
```cpp
using itType = std::vector<std::string>::iterator;
template<typename T>
using arr12 = std::array<T,12>; // template for multiple aliases

```

## enumeration 
```cpp
enum Old1 {yes, no, maybe}; // traditional form
enum class New1 {never, sometimes, often, always}; // new form
enum struct New2 {never, lever, sever}; // new form
```

## class change
```cpp
class Plebe
{
Plebe(int); // automatic int-to-plebe conversion
explicit Plebe(double); // requires explicit use
...
};
...
Plebe a, b;
a = 5; // implicit conversion, call Plebe(5)
b = 0.5; // not allowed
b = Plebe(0.5); // explicit conversion
```

[[chapter11|explicit in class]]
# new feature
## special member  functions
```cpp
Someclass::Someclass(const Someclass &); // defaulted copy constructor
Someclass::Someclass(Someclass &&); // defaulted move constructor

Someclass & Someclass::operator(const Someclass &); // defaulted copy assignment
Someclass & Someclass::operator(Someclass &&); // defaulted move assignment
```

## delete and defaulted
```cpp
Someclass(Someclass &&);
Someclass() = default; // use compiler-generated default constructor
Someclass(const Someclass &) = default;
Someclass & operator=(const Someclass &) = default;

Someclass() = default; // use compiler-generated default constructor
// disable copy constructor and copy assignment operator:
Someclass(const Someclass &) = delete;
Someclass & operator=(const Someclass &) = delete;
// use compiler-generated move constructor and move assignment operator:
Someclass(Someclass &&) = default;
Someclass & operator=(Someclass &&) = default;
Someclass & operator+(const Someclass &) const;

//difference between move and copy
Someclass three(one); // not allowed, one an lvalue
Someclass four(one + two); // allowed, expression is an rvalue
```

## constructor delegation
```cpp
public:
Notes();
Notes(int);
Notes(int, double);
Notes(int, double, std::string);
};
Notes::Notes(int kk, double xx, std::string stt) : k(kk),
x(xx), st(stt) {/*do stuff*/}
Notes::Notes() : Notes(0, 0.01, "Oh") {/* do other stuff*/}
Notes::Notes(int kk) : Notes(kk, 0.01, "Ah") {/* do yet other stuff*/ }
Notes::Notes( int kk, double xx ) : Notes(kk, xx, "Uh") {/* ditto*/ }
```

## manage virtual methods
### override 
*use the virtual specifier override to indicate that you intend to override a virtual function. Place it after the parameter list*
### final
*prohibit derived classes from overriding a particular virtual method,place final after the parameter list*
# lambda functions
## function pointers,functors , and lambdas
```cpp
// function pointer
int count3 = std::count_if(numbers.begin(), numbers.end(), f3);
cout << "Count of numbers divisible by 3: " << count3 << '\n';
int count13 = std::count_if(numbers.begin(), numbers.end(), f13);
cout << "Count of numbers divisible by 13: " << count13 << "\n\n";
```

[[chapter16#^3b63ef|functor]]
```cpp
// functors
class f_mod
{
	private:
	int dv;
	public:
	f_mod(int d = 1) : dv(d) {}
	bool operator()(int x) {return x % dv == 0;}
};
```

### lambda
```cpp
count3 = std::count_if(numbers.begin(), numbers.end(),
[](int x){return x % 3 == 0;});
```
[[lambda.cpp|example code]]
```cpp
// reuse the lambda code
auto mod3 = [](int x){return x % 3 == 0;} // mod3 a name for the lambda
count1 = std::count_if(n1.begin(), n1.end(), mod3);
count2 = std::count_if(n2.begin(), n2.end(), mod3);
```

# wrapper
```cpp
std::function<double(char,int)>fdci;
//  a function pointer 
double dub(double x) {return 2.0*x;}
double square(double x) {return x*x;}
function<double(double)> ef1 = dub;
function<double(double)> ef2 = square;
```

*function signature consists of return type and a list of parameters*

# variadic templetes(多参数模板)
## function parameter packs
```cpp
template<typename... Args> // Args is a template parameter pack
void show_list1(Args... args) // args is a function parameter pack
```

*the function pack args contains a list of values that matches the list of types in the template pack Args, both in type and in number*
>[!question]
>unpacking the packs

## using recursion in VTF
```CPP
template<typename T, typename... Args>
void show_list3( T value, Args... args)
{
std::cout << value << ", ";
show_list3(args...);
}
```

# more features
## concurrent programming
>[!keyword]
>The keyword ==thread_local== is used to declare variables having static storage duration relative to a particular thread; that is, they expire when the thread in which they are defined expires

