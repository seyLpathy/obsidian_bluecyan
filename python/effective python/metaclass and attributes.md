# use plain attributes

[[dynamic attributes and properties#^07c5b7|@property]]

```python
class BoundedResistance(Resistor):
def __init__(self, ohms):
	super().__init__(ohms)
@property
def ohms(self):
	return self._ohms
@ohms.setter
def ohms(self, ohms):
	if ohms <= 0:
		raise ValueError(f'ohms must be > 0; got {ohms}')
	self._ohms = ohms
```

✦ Define new class interfaces using simple public attributes and avoid defining setter and getter methods.
✦ Use @property to define special behavior when attributes are accessed on your objects, if necessary.
✦ Follow the rule of least surprise and avoid odd side effects in your @property methods.
✦ Ensure that @property methods are fast; for slow or complex work—especially involving I/O or causing side effects—use normal methods instead.
# using the @property 
[[Bucket.py|demo code]]
✦ Use @property to give existing instance attributes new functionality.
✦ Make incremental progress toward better data models by using @property.
✦ Consider refactoring a class and all call sites when you find yourself using @property too heavily
# using descriptor for reusable @property methods
[[attribute Descriptor|related reference]]
## the working logic for descriptor
instance.attribute --> class.attribute-->namesake class object with get/set/ method
and follow the descriptor protocol
## getattribute >> getattr

# validate subclasses 
## define a metaclass
1. inerinting from type
2. receive the contents of associated class statements in its \_\_new\_\_ method
## using the \_\_init_subclass\_\_
```python
class BetterPolygon:
	sides = None # Must be specified by subclasses
	def __init_subclass__(cls):
		super().__init_subclass__()
		if cls.sides < 3:
			raise ValueError('Polygons need 3+ sides')
```
✦ The __new__ method of metaclasses is run after the class statement’s entire body has been processed.
✦ Metaclasses can be used to inspect or modify a class after it’s
defined but before it’s created, but they’re often more heavyweight
than what you need.
✦ Use __init_subclass__ to ensure that subclasses are well formed
at the time they are defined, before objects of their type are
constructed.
✦ Be sure to call super().__init_subclass__ from within your class’s
__init_subclass__ definition to enable validation in multiple layers
of classes and multiple inheritance.
# register class with  \_\_init\_subclass\_\_
[[serializable.py|demo code]]
✦ Class registration is a helpful pattern for building modular Python
programs.
✦ Metaclasses let you run registration code automatically each time a
base class is subclassewrapd in a program.
✦ Using metaclasses for class registration helps you avoid errors by
ensuring that you never miss a registration call.
✦ Prefer __init_subclass__ over standard metaclass machinery because it’s clearer and easier for beginners to understand
# annotate class attributes with \_\_set\_name\_\_
```python
class Field:
	def __init__(self):
		self.name = None
		self.internal_name = None
	def __set_name__(self, owner, name):
		# Called on class creation for each descriptor
		self.name = name
		self.internal_name = '_' + name
	def __get__(self, instance, instance_type):
		if instance is None:
			return self
		return getattr(instance, self.internal_name, '')
	def __set__(self, instance, value):
		setattr(instance, self.internal_name, value)
```
✦ Metaclasses enable you to modify a class’s attributes before the class is fully defined.
✦ Descriptors and metaclasses make a powerful combination for declarative behavior and runtime introspection.
✦ Define __set_name__ on your descriptor classes to allow them to take into account their surrounding class and its property names.
# class decorator over metaclass 
✦ A class decorator is a simple function that receives a class instance
as a parameter and returns either a new class or a modified version
of the original class.
✦ Class decorators are useful when you want to modify every method
or attribute of a class with minimal boilerplate.
✦ Metaclasses can’t be composed together easily, while many class
decorators can be used to extend the same class without conflicts.