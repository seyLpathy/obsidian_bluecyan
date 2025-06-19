# using the class over the nested structure

✦ Avoid making dictionaries with values that are dictionaries, long tuples, or complex nestings of other built-in types.
✦ Use namedtuple for lightweight, immutable data containers before you need the flexibility of a full class.
✦ Move your bookkeeping code to using multiple classes when your internal state dictionaries get complicated.

## nametuple demo

```python
from collections import nametuple
User=nametuple('User',['name','sex','age'])
user=User(name="kongxx",sex='male',age=21)
user=User._make(['kongxx','male',21])
```

# accept functions instead of classes

```python
from collections import defaultdict
current={'green':12,'blue':3}
increments=[
	('red',5),
	('blue',17),
	('orange',9),
]
result = defaultdict(log_missing, current)
print('Before:', dict(result))
for key, amount in increments:
	result[key] += amount
print('After: ', dict(result))
```

# use @classmethod to contruct objects generically

✦ Python only supports a single constructor per class: the \_\_init\_\_ method.
✦ Use [[decorator#^f3813c|@classmethod]] to define alternative constructors for your classes.
✦ Use class method polymorphism to provide generic ways to build and connect many concrete subclasses.

# initial parent class with super

Python’s standard method resolution order ([[class metaprogramming#^90f5da|MRO]]) solves the problems of superclass initialization order and diamond inheritance.
✦ Use the super built-in function with zero arguments to initialize parent classes.

# compose functionality with Mix-in classes

wait for implementation

# public attribute over private ones

1. using double underscore to create a private attribute
2. directly accessing private fields from the outside the class raises an exception
3. a subclass can't access its partent class's field
```python
class MyOtherObject:
	def __init__(self):
		self.__private_field = 71
	@classmethod
	def get_private_field_of_instance(cls, instance):
		return instance.__private_field
```
# inherit from collections.abc for custom container
[[python/fluent_python/data structure#^27b031|special functions]]
[[interface to ABC|inherit the abstract base class]]
