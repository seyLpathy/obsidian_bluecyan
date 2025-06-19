## slice object
### keypoint
1. slice is a built-in object
2. attributes **start,stop, and step and indices methods**
```python
def __getitem__(self, index):
	cls = type(self)
	if isinstance(index, slice):
		return cls(self._components[index])
	elif isinstance(index, numbers.Integral):
		return self._components[index]
	else:
		msg = '{cls.__name__} indices must be integers'
		raise TypeError(msg.format(cls=cls))
```
### dynamic attribute access
\_\_getattr\_\_ check whether the attribute being sought is one of the letters xyzt
>[!attention]
> this function only works when fail to find the specific attribute as find with object. 
```python
shortcut_names = 'xyzt'
def __getattr__(self, name):
	cls = type(self)
	if len(name) == 1:
		pos = cls.shortcut_names.find(name)
		if 0 <= pos < len(self._components):
			return self._components[pos]
		msg = '{.__name__!r} object has no attribute {!r}'
	raise AttributeError(msg.format(cls, name))
```

```python
# set attr 
def __setattr__(self,name,value):
	cls=type(self)
	if len(name)==1:
		if name in cls.shortcut_names:
			error='readonly attributes {attr_name!r}'
		elif name.islower():
			error = "can't set attributes 'a' to 'z' in {cls_name!r}"
		else:
			error = ''
		if error:
			msg = error.format(cls_name=cls.__name__, attr_name=name)
			raise AttributeError(msg)
	super().__setattr__(name, value)
```
## hashing and faster
```python
class Vector:
	typecode = 'd'
	# many lines omitted in book listing...
	def __eq__(self, other): #
		return tuple(self) == tuple(other)
	def __hash__(self):
		hashes = (hash(x) for x in self._components) #
		return functools.reduce(operator.xor, hashes, 0) #
```