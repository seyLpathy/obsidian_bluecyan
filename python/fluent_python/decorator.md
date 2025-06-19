>[!keypoint]
 >function decorators are executedas soon as the module is imported, but the decorated functions only run when they are explicitly invoked. ==This highlights the difference between what Pythonistas call import time and runtime.==
 
 ```python
 ## decorator-enhanced strategy pattern
promos=[] 
def promotion(promo_func):
	promos.append(promo_func)
	return promo_func

@promotion
def anypromostrategy():
	pass
def best_promo(order):
	return max(promo(order) for promo in promos)
```
## variable scope rule
1. Python does not require you to declare variables,but assumes that a variable assigned in the body of a function is local
2. use the keyword *global* to treat a variable defined in a function body as global variable
## closure
![alt text](python/fluent_python/image.png)
>[!summary]
>a closure is a function that retains the bindings of the free variables that exist when the function is defined, so that they can be used later when the function is invoked and the defining scope is no longer available
## generic functions 
```python
import html
def htmlize(obj):
	return '<pre>{}</pre>'.format((content))
```
*using the @singledispatch to decorate a plain function to transfer it into generic function*
![alt text](python/fluent_python/image-1.png)

## stacked decorator
```python
@d1
@d2
def f():
	print('f')
```
## parameterized decorators
==make a decorator factory that takes those arguments and returns a decorator, which is then applied to the function to be decorated==
```python
def register(active=True):
	def decorate(func):
		print('running register(active=%s)->decorate(%s)'
				% (active, func))
		if active:
			registry.add(func)
		else:
			registry.discard(func)
		return func
return decorate
@register(active=False)
def f1():
print('running f1()')
@register()
def f2():
print('running f2()')
def f3():
print('running f3()')
```

## @classmethod and @staticmethod

^f3813c

### the @classmethod
1. first argument is the cls,reference to the class this method within
2. any subclass can obtain the @classmethod methods
3. most time  use as a factory to create instance
### the @staticmethod
1. decorated methods becomes a plain function with any boundary of specific class
2. if the purpose was to create a factory then you must use the @classmethod

```python
class Date(object):
    
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999

date2 = Date.from_string('11-09-2012')
is_date = Date.is_date_valid('11-09-2012')
```
```