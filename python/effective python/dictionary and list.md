# catch all unpacking over slicing

```python
car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
oldest, second_oldest, *others = car_ages_descending
# using the starred expression to receive all values that did not mathc any other part
# if no catch up then it will be empty list
```

# the sort methods

```
tools.sort(key=lambda x: x.name)
# sort by the function user-difined
```

# the dictionary insertion

The way that dictionaries preserve insertion ordering is now part of
the Python language specification

```python
class MyClass:
def __init__(self):
	self.alligator = 'hatchling'
	self.elephant = 'calf'
a = MyClass()
for key, value in a.__dict__.items():
	print(f'{key} = {value}')
>>>
alligator = hatchling
elephant = calf
```

# get over in and keyError to handle Missing dictionary keys

```python
	try:
		names = votes[key]
	except KeyError:
		votes[key] = names = []
	names.append(who)
## the get function of a dict
names=votes.get(key)
if names is None:
	votes[key]=names=[]
names.append(who)
```

# use defaultdict over setdefault

```python
## add a new item by setdefault
from collections import defaultdict
visiter={
	'mexico':{'Tulum','Puerto Vallarto'},
	'Japan':{'Hakone'},
}
visiter.setdefault('France',set()).add('Arles')
print(visiter)
class Visits:
	def __init__(self):
		self.data=defaultdict(set)## create a default empty set as dict
	def add(self,country,city):
		self.data[country].add(city)
visits=Visits()
visits.add('England',"London")
visits.add('America',"New York")
print(visits.data)
```

# subclass the dict and implements the **Miss** method

```python
class Picture(dict):
	def__missing__(self,key):
	## this function wiil be called when the specific key is not found
	## the second time  the same key retrival will not call this function any more
		value=open_picture(key)
		self[key]=value
		return value
pictures=Pictures()
handle=pictures[path]
handle.seek(0)
image_data=handle.read()
```
