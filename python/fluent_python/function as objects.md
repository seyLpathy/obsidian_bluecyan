>[!example]

```python
def factorial(n):
	'''returns n!'''
		return 1 if n < 2 else n * factorial(n-1)
factorial.__doc__
type(factorial)
```

## seven flavors of callable objects
1. def /lambda
2. built in functions (len time.strftime)
3. dict.get
4. functions defined in the body of a class
5.  classes (\_\_new\_\_)
6. class instances
7. generator functions (yield keyword to return a generator object)
### user-defined callable types
implementing a \_\_call\_\_ instance methods in a class
### function instropection
```python
dir(factorial)
['__annotations__', '__call__', '__class__', '__closure__', '__code__',
'__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
 '__format__', '__ge__', '__get__', '__getattribute__', '__globals__',
'__gt__', '__hash__', '__init__', '__kwdefaults__', '__le__', '__lt__',
'__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__',
'__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
'__subclasshook__']

# listing attributes of functions that don't exist in plain instances
class C: pass
obj=C()
def func(): pass
sorted(set(dir(func))-set(dir(obj)))
```

![[Pasted image 20240612164115.png]]

#### positional to keyword-only parameters
```python
def tag(name, *content, cls=None, **attrs):
"""Generate one or more HTML tags"""
	if cls is not None:
		attrs['class'] = cls
	if attrs:
		attr_str = ''.join(' %s="%s"' % (attr, value)
						for attr, value
						in sorted(attrs.items()))
	else:
		attr_str = ''
	if content:
		return '\n'.join('<%s%s>%s</%s>' %
						(name, attr_str, c, name) for c in content)
	else:
		return '<%s%s />' % (name, attr_str)
```

\*content类似于列表捕捉参数
\*\*attrs类似于词典捕捉参数
cls捕捉关键字参数

#### 获取参数信息
```python
clip.__defaults__

clip.__code__.co_varnames
# 参数和本地参数
clip.__code__.co_argcount
# 参数个数

```

### function annotations
```python
def clip(text:str, max_len:'int > 0'=80) -> str:
	"""Return text clipped at the last space before or after max_len
	"""
clip.__annotations__
```

## packages for functional programming
### the operator module
```python
from functools import reduce
def fact(n):
		return reduce(lambda a,b: a*b,range(1,n+1))
```
### itemgetter and attrgetter 
get  items and attributes from class
```python
from city in sorted(metro_data,key=itemgetter(1)):
```
### partial 
partial using the function
```python
from operator import mul
from functions import partial
triple=partial(mul,3)
triple(7)
'''21'''
```
*partial takes the first callable as first argument,followed by an arbitrary number of positional and keyword arguments to bind.*
