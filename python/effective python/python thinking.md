# get your python version

```shell
$ python --version
```

```python
import sys
print(sys.version)
```

# follow the PEP 8 style

## space

1. use space as indentation
2. four spaces for each level of significant indenting
3. lines should be 79 characters or less
4. functions and classes should be separated by two blank lines
5. in a class, methods should be separated by a single blank line
6. put only space before and after the = operator in a variable assignment

## naming

1. functions,variable and attributes should be in lowercase_underscore format
2. Module-level constants should be in ALL_CAPS format.
3. Class methods should use cls, which refers to the class, as the name of the first parameter. ##　 expression and statement
4. use inline negation
5. using not instead of len() for empty container check
6. avoid single-line if statemen

## import

1. Always use absolute names for modules when importing them
2. import order: stand library modules,third party modules,your own modules

# byte and str

```python
a = b'h\x65llo'
print(list(a))
print(a)
## function to convert between byte and str
def to_str(bytes_or_str):
	if isinstance(bytes_or_str, bytes):
		value = bytes_or_str.decode('utf-8')
	else:
		value = bytes_or_str
	return value # Instance of str
print(b'one' + b'two')
print('one' + 'two')
```

# f-strings over c-style format strings

## c-style %

```python
a = 0b10111011
b = 0xc5f
print('Binary is %d, hex is %d' % (a, b))
>>>
Binary is 187, hex is 3167
```

## python %

```python
key = 'my_var'
value = 1.234
old_way = '%-10s = %.2f' % (key, value)
new_way = '%(key)-10s = %(value).2f' % {
'key': key, 'value': value} # Original
reordered = '%(key)-10s = %(value).2f' % {
'value': value, 'key': key} # Swapped
assert old_way == new_way == reordered
```

## the format built-in and str.format

```python
a = 1234.5678
formatted = format(a, ',.2f')
print(formatted)
b = 'my string'
formatted = format(b, '^20s')
print('*', formatted, '*')
key = 'my_var'
value = 1.234
formatted = '{} = {}'.format(key, value)
print(formatted)
>>>
my_var = 1.234
formatted = '{:<10} = {:.2f}'.format(key, value)
## provide a colon character followed by format specifiers
print(formatted)
>>>
my_var = 1.23
print('{} replaces {{}}'.format(1.23))
>>>
1.23 replaces {}
formatted = '{1} = {0}'.format(key, value)
## position change
formatted = '{0} loves food. See {0} cook.'.format(name)
## multitimes reference
```

## the f-string

```python
key = 'my_var'
value = 1.234
formatted = f'{key!r:<10} = {value:.2f}'
print(formatted)
>>>
'my_var' = 1.23

## example
f_string = f'#{i+1}: {item.title():<10s} = {round(count)}'
## placeholder nested
places = 3
number = 1.23456
print(f'My number is {number:.{places}f}')
```

# helper function

```python
def get_first_int(values, key, default=0):
	found = values.get(key, [''])
	if found[0]:
	return int(found[0])
		return default
```

Move complex expressions into helper functions, especially if you need to use the same logic repeatedly

# unpacking

```python
item = ('Peanut butter', 'Jelly')
first, second = item # Unpacking
print(first, 'and', second)
>>>
Peanut butter and Jelly
```

## swap items

```python
def bubble_sort(a):
	for _ in range(len(a)):
		for i in range(1, len(a)):
			if a[i] < a[i-1]:
				a[i-1], a[i] = a[i], a[i-1] # Swap
names = ['pretzels', 'carrots', 'arugula', 'bacon']
bubble_sort(names)
print(names)
>>>
['arugula', 'bacon', 'carrots', 'pretzels']
```

# prefer enumerate over range

```python
flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
it = enumerate(flavor_list)
print(next(it))
print(next(it))
>>>
(0, 'vanilla')
(1, 'chocolate')
for i, flavor in enumerate(flavor_list, 1):
	print(f'{i}: {flavor}')
```

# zip and itertools.zip_longest

```python
names = ['Cecilia', 'Lise', 'Marie']
counts = [len(n) for n in names]
for name, count in zip(names, counts):
	if count > max_count:
		longest_name = name
		max_count = count
```
