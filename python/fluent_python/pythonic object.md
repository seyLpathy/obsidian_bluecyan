## object representation

> [!definition]
> repr()
> Return a string representing the object as the >developer wants to see it.
>
> str()
> Return a string representing the object as the >user wants to see it.

## vector class Redux

```python
from array import array
import math
class Vector2d:
	typecode='d'
	def __init__(self, x, y):
		self.x = float(x)
		self.y = float(y)
	def __iter__(self):   #makes unpacking work
		return (i for i in (self.x, self.y))
	def __repr__(self):
		class_name = type(self).__name__
		return '{}({!r}, {!r})'.format(class_name, *self)
	def __str__(self):
		return str(tuple(self))
	def __bytes__(self):
		return (bytes([ord(self.typecode)]) +
			bytes(array(self.typecode, self)))
	def __eq__(self, other):
		return tuple(self) == tuple(other)
	def __abs__(self):
		return math.hypot(self.x, self.y)
	def __bool__(self):
		return bool(abs(self))
```

## alternative constructor

### classmethod example

```python
# classmethod
@classmethod
def frombytes(cls, octets):
typecode = chr(octets[0])
memv = memoryview(octets[1:]).cast(typecode)
return cls(*memv)
```

### contrast

```python
>>> class Demo:
... @classmethod
... def klassmeth(*args): # first argument will always be class
... return args #
... @staticmethod
... def statmeth(*args):
... return args #
...
>>> Demo.klassmeth() #
(<class '__main__.Demo'>,)
>>> Demo.klassmeth('spam')
(<class '__main__.Demo'>, 'spam')
>>> Demo.statmeth() #
()
```

## format display

```python
>>> brl = 1/2.43 # BRL to USD currency conversion rate
>>> brl
0.4115226337448559
>>> format(brl, '0.4f') #
'0.4115
>>> '1 BRL = {rate:0.2f} USD'.format(rate=brl) #
'1 BRL = 0.41 USD'
>>> format(42, 'b')
'101010'
>>> format(2/3, '.1%')
'66.7%'
```

_If a class has no \_\_format\_\_, the method inherited from object returns str(my_ob
ject)._

## private and protected attributes

![alt text](python/fluent_python/image-6.png)

```python
>>> v1 = Vector2d(3, 4)
>>> v1.__dict__
{'_Vector2d__y': 4.0, '_Vector2d__x': 3.0}
>>> v1._Vector2d__x
3.0
```

## saving space with **slot** class

```python
class Vector2d:
__slots__ = ('__x', '__y')
typecode = 'd'
# methods follow (omitted in book listing)
```
