# using generator instead of list

```
def index_words(text):
	if text:
		yield 0
		for index, letter in enumerate(text):
			if letter == ' ':
				yield index+1
```

# generator expression

``python
it =(len(x) for x in open('my_file.txt))
print(it)

# compose multiple generator with yield from

[[the iterator]]

## the yield from expression

```python
def animate_composed():
	yield from move(4, 5.0)# iterate over the whole iterator
	yield from pause(3)
	yield from move(2, 3.0)
```

## the send function for generator

[[coroutines]]
variable=yield can send data to the iterator and obtain the control flow

```python
def wave_modulating(steps):
	step_size = 2 * math.pi / steps
	amplitude = yield # Receive initial amplitude
	for step in range(steps):
		radians = step * step_size
		fraction = math.sin(radians)
		output = amplitude * fraction
		amplitude = yield output # Receive next amplitude
def run_modulating(it):
	amplitudes = [
		None, 7, 7, 7, 2, 2, 2, 2, 10, 10, 10, 10, 10]
	for amplitude in amplitudes:
		output = it.send(amplitude)
		transmit(output)
```

> [!summary]
> wrap the input of a generator and built-in next method together

# avoid causing state transitions in generator with throw

✦ The throw method can be used to re-raise exceptions within generators at the position of the most recently executed yield expression.
✦ Using throw harms readability because it requires additional nesting and boilerplate in order to raise and catch exceptions.
✦ A better way to provide exceptional behavior in generators is to use
a class that implements the \_\_iter\_\_ method along with methods to cause exceptional state transitions

![[Pasted image 20240630124630.png]]

# itertools for working with iterators and Generators

## built-in functions
[[the iterator#^bf5d0e|functions]]
### linking together

1. chain
2. repeat
3. cycle # cycle forever
4. tee # split a single iterator into the number of parallel iterators
5. zip_longest

### filtering items from an iterator

1. islice
   Use islice to slice an iterator by numerical indexes without copying
2. takewhile

```python
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
less_than_seven = lambda x: x < 7
it = itertools.takewhile(less_than_seven, values)
print(list(it))
>>>
[1, 2, 3, 4, 5, 6]
```

3. dropwhile
   which is the opposite of takewhile, skips items from an iterator until the predicate function returns True for the first time

### producing combinations of Items form iterator

1. accumulate
2. product

```python
single = itertools.product([1, 2], repeat=2)
print('Single: ', list(single))
multiple = itertools.product([1, 2], ['a', 'b'])
print('Multiple:', list(multiple))
>>>
Single: [(1, 1), (1, 2), (2, 1), (2, 2)]
Multiple: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
```

3. permutations
   returns the unique ordered permutations of length N with items from an iterator:

```python
it = itertools.permutations([1, 2, 3, 4], 2)
print(list(it))
```
