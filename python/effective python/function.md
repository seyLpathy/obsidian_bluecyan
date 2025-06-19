# never unpack the function returns over three variables

# raising exceptions to returning None

```python
def careful_divide(a: float, b: float) -> float:
"""Divides a by b.
	Raises:
	ValueError: When the inputs cannot be divided.
"""
	try:
		return a / b
	except ZeroDivisionError as e:
		raise ValueError('Invalid inputs')
```

# variable positional arguments

Functions can accept a variable number of positional arguments by using _args in the def statement.
✦ You can use the items from a sequence as the positional arguments
for a function with the _ operator.
✦ Using the * operator with a generator may cause a program to run
out of memory and crash.
✦ Adding new positional parameters to functions that accept *args
can introduce hard-to-detect bugs

# keyword argument

==1. Positional arguments must be specified before keywrod arguments.==
==2. each argument can specified only once.==
==3. using the \*\* operator to pass the dictionary as arguments==

```
def remainder(number, divisor):
	return number % divisor
my_kwargs = {
'number': 20,
'divisor': 7,
}
assert remainder(**my_kwargs) == 6
my_kwargs = {
'divisor': 7,
}
assert remainder(number=20, **my_kwargs) == 6
## the default value
def flow_rate(weight_diff, time_diff):
	return weight_diff / time_diff
weight_diff = 0.5
time_diff = 3
def flow_rate(weight_diff, time_diff, period=1):
	return (weight_diff / time_diff) \* period
```

# use None and Docstrings to specify Dynamic Default Arguments

```
def log(message, when=None):
"""Log a message with a timestamp.
Args:
message: Message to print.
when: datetime of when the message occurred.
Defaults to the present time.
"""
	if when is None:
		when = datetime.now()
	print(f'{when}: {message}')
```

# keyword-only and Positional-only Arguments

```python
def safe_division_e(numerator, denominator, /,
	ndigits=10, *, # Changed
	ignore_overflow=False,
	ignore_zero_division=False):
	# the / in arguments list marks the end of only positonal arguments
	# any argument between / and * passed by positional or keyword argument
	try:
		fraction = numerator / denominator # Changed
		return round(fraction, ndigits) # Changed
	except OverflowError:
		if ignore_overflow:
			return 0
		else:
			raise
	except ZeroDivisionError:
		if ignore_zero_division:
			return float('inf')
		else:
			raise
```
# the decorator
```python
# the decorator function
def trace(func):
	def wrapper(*args, **kwargs):
		result = func(*args, **kwargs)
		print(f'{func.__name__}({args!r}, {kwargs!r}) '
			f'-> {result!r}')
		return result
	return wrapper
## the decorated functions
@trace
def fibonacci(n):
	"""Return the n-th Fibonacci number"""
	if n in (0, 1):
		return n
	return (fibonacci(n - 2) + fibonacci(n - 1))
## use the wrapper from functools
from functools import wraps
def trace(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
	...
	return wrapper
@trace
def fibonacci(n):
	...
```