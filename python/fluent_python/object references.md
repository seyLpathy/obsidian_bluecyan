## variable are not boxes
```python
a=[1,2,3]
b=a
a.append(4)
b
[1,2,3,4]
```
![alt text](python/fluent_python/image-2.png)
## identify,equality,and aliases
```python
>>> charles = {'name': 'Charles L. Dodgson', 'born': 1832}
>>> lewis = charles
>>> lewis is charles  ## assign means alias
True
>>> id(charles), id(lewis)
(4300473992, 4300473992)
>>> lewis['balance'] = 950
>>> charles
{'name': 'Charles L. Dodgson', 'balance': 950, 'born': 1832}
>>> alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
>>> alex == charles
True
>>> alex is not charles
True
```
![alt text](python/fluent_python/image-3.png)

### summary
id() is() can confirm the alias and identity 

1. \=\= compare the values of object while *is* compares their identities.
2. a==b equal to type-dependent \_\_eq\_\_ implemetation
### relative immutability of tuples
```python
>>> t1 = (1, 2, [30, 40])
>>> t2 = (1, 2, [30, 40])
>>> t1 == t2
True
>>> id(t1[-1])
4302515784
>>> t1[-1].append(99)
>>> t1
(1, 2, [30, 40, 99])
>>> id(t1[-1])
4302515784
>>> t1 == t2
False
```
## default shallow copies
```python
>>> l1 = [3, [55, 44], (7, 8, 9)]
>>> l2 = list(l1)
>>> l2
[3, [55, 44], (7, 8, 9)]
>>> l2 == l1
True
>>> l2 is l1
False

l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = list(l1) #
l1.append(100) #
l1[1].remove(55) #
print('l1:', l1)
print('l2:', l2)
l2[1] += [33, 22] #
l2[2] += (10, 11) #
print('l1:', l1)
print('l2:', l2)
```
![alt text](python/fluent_python/image-4.png)
![alt text](python/fluent_python/image-5.png)

### deep copy
```python
>>> import copy
>>> bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
>>> bus2 = copy.copy(bus1)
>>> bus3 = copy.deepcopy(bus1)
>>> id(bus1), id(bus2), id(bus3)
(4301498296, 4301499416, 4301499752)
>>> bus1.drop('Bill')
>>> bus2.passengers
['Alice', 'Claire', 'David']
>>> id(bus1.passengers), id(bus2.passengers), id(bus3.passengers)
(4302658568, 4302658568, 4302657800)
>>> bus3.passengers
['Alice', 'Bill', 'Claire', 'David']
```
## function parameters as reference
```python
>>> bus1 = HauntedBus(['Alice', 'Bill'])
>>> bus1.passengers
['Alice', 'Bill']
>>> bus1.pick('Charlie')
>>> bus1.drop('Alice')
>>> bus1.passengers
['Bill', 'Charlie']
>>> bus2 = HauntedBus()
>>> bus2.pick('Carrie')
>>> bus2.passengers
['Carrie']
>>> bus3 = HauntedBus()
>>> bus3.passengers
['Carrie']
>>> bus3.pick('Dave')
>>> bus2.passengers
['Carrie', 'Dave']
>>> bus2.passengers is bus3.passengers
True
>>> bus1.passengers
['Bill', 'Charlie']
```

```python
>>> dir(HauntedBus.__init__) # doctest: +ELLIPSIS
['__annotations__', '__call__', ..., '__defaults__', ...]
>>> HauntedBus.__init__.__defaults__
(['Carrie', 'Dave'],)
>>> HauntedBus.__init__.__defaults__[0] is bus2.passengers
True
```

### defensive programming
```python
def __init__(self, passengers=None):
if passengers is None:
	self.passengers = []
else:
	self.passengers = list(passengers)
## deepcopy 
```
## del and garbage collections
```python
>>> import weakref
>>> s1 = {1, 2, 3}
>>> s2 = s1
>>> def bye():
... print('Gone with the wind...')
...
>>> ender = weakref.finalize(s1, bye)
>>> ender.alive
True
>>> del s1  #del does not delete an object, just a reference to it
>>> ender.alive
True
>>> s2 = 'spam' #Rebinding the last reference,s2, makes {1, 2, 3} unreachable. It is destroyed,the bye callback is invoked, and ender.alive becomes False.
Gone with the wind...
>>> ender.alive
False
```
