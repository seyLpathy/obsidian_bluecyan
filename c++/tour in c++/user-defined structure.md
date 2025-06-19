## Union
```cpp
union Value{
	Node* p;
	int i;
};
struct Entry{
	 string name;
	 Type t;
	 Value v;
}
```

## variant
```cpp
std::variant<int,float> v,w
```