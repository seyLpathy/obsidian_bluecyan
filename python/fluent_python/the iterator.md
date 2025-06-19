## why sequence are iterable
1. whether implements \_\_iter\_\_
2. whether implements \_\_getitem\_\_,python creates an terator aht attempts to fetch items
3. type error if the above 2 not implemented
4. the \_\_subclasshook\_\_ is implemented by the abc.Iterable
### the iterator VS iterable
```python
s = 'ABC'
>>> it = iter(s) #
>>> while True:
... try:
... print(next(it)) #
... except StopIteration: #
... del it #
... break #
```

### the standard interface for an iterator 
1.  \_\_next\_\_  Returns the next available item, raising StopIteration when there are no more items.
2. \_\_iter\_\_ Returns self; this allows iterators to be used where an iterable is expected, for example, in a for loop.
>[!summary]
>iterables have an __iter__ method that instantiates a new iterator every time.
Iterators implement a __next__ method that returns individual items, and an __iter__
method that returns self.
## generator
### how it works
1. a generator contains a yield keyword
2. when invoked return agenerator object
3. Generators are iterators that produce the values of the expressions passed to
yield.
4. When the body of the function completes, the generator object raises a StopIteration

```python
>>> def gen_AB(): #
... print('start')
... yield 'A' #  stop the first call to generator
... print('continue')
... yield 'B' #  stop the second call to generator
... print('end.') #
...
>>> for c in gen_AB(): #
... print('-->', c)
```

```python
>>> gen = itertools.takewhile(lambda n: n < 3, itertools.count(1, .5))
>>> list(gen)
[1, 1.5, 2.0, 2.5]
>>> import itertools
>>> gen = itertools.count(1, .5)
>>> next(gen)
1
>>> next(gen)
1.5
>>> next(gen)
2.0
>>> next(gen)
2.5
```

![[Pasted image 20240620225033.png]]


```python
>>> def vowel(c):
... return c.lower() in 'aeiou'
...
>>> list(filter(vowel, 'Aardvark'))
['A', 'a', 'a']
>>> import itertools
>>> list(itertools.filterfalse(vowel, 'Aardvark'))
['r', 'd', 'v', 'r', 'k']
>>> list(itertools.dropwhile(vowel, 'Aardvark'))
['r', 'd', 'v', 'a', 'r', 'k']
>>> list(itertools.takewhile(vowel, 'Aardvark'))
['A', 'a']
>>> list(itertools.compress('Aardvark', (1,0,1,1,0,1)))
['A', 'r', 'd', 'a']
>>> list(itertools.islice('Aardvark', 4))
['A', 'a', 'r', 'd']
>>> list(itertools.islice('Aardvark', 4, 7))
['v', 'a', 'r']
>>> list(itertools.islice('Aardvark', 1, 7, 2))
['a', 'd', 'a']
```
## reduced functions
![[Pasted image 20240621125515.png]]
![[Pasted image 20240621125727.png]] ^bf5d0e
```python
>>> def d6():
... return randint(1, 6)
...
>>> d6_iter = iter(d6, 1)
>>> d6_iter
<callable_iterator object at 0x00000000029BE6A0>
>>> for roll in d6_iter:
... print(roll)
```

## generator for database conversion
left blank by purpose