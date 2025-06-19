## abc in the standard library

![alt text](python/fluent_python/image-7.png)

1. iterable => \_\_iter\_\_
2. contains => in operator
3. sized => \_\_len\_\_
4. Sequence, Mapping, and Set each has a mutable version
5. .items(), .keys(),and .values() inherit from ItemsView, ValuesView, and ValuesView

### the number tower of abcs

. Number
. Complex
. Real
. Rational
. Integral

## abc practice

![alt text](python/fluent_python/image-8.png)
![alt text](python/fluent_python/image-9.png)
## hook
```python
class Sized(metaclass=ABCMeta):
	__slots__ = ()
	@abstractmethod
	def __len__(self):
		return 0
	@classmethod
	def __subclasshook__(cls, C):
	if cls is Sized:
		if any("__len__" in B.__dict__ for B in C.__mro__): #
			return True #
	return NotImplemented #
	```