# each block in try/except/else/finally

## finally block

code will be excuted before the error raised

```python
def try_finally_example(filename):
	print('* Opening file')
handle = open(filename, encoding='utf-8') # Maybe OSError
try:
	print('* Reading data')
	return handle.read() # Maybe UnicodeDecodeError
finally:
	print('* Calling close()')
	handle.close() # Always runs after try bloc
```

## else blocks

when the try block doesn't raise an exception, the else block runs.The else clause ensures that what follows the try/except is visually distinguished from the except block.

```python
import json
def load_json_key(data, key):
	try:
		print('* Loading JSON data')
		result_dict = json.loads(data) # May raise ValueError
	except ValueError as e:
		print('* Handling ValueError')
		raise KeyError(key) from e
	else:
		print('* Looking up key')
		return result_dict[key] # May raise KeyError
```
# contextlib and with statements for reusable try/finally behavior
## set the context with contextlib
[[contextlogging.py|demo code]]
## using with targets
```python
with log_level(logging.DEBUG, 'my-log') as logger:
	logger.debug(f'This is a message for {logger.name}!')
	logging.debug('This will not print')
logger = logging.getLogger('my-log')
logger.debug('Debug will not print')
logger.error('Error will print')
```

# use datetime instead of time
## the time module
```python
import time
now = 1552774475
local_tuple = time.localtime(now)
time_format = '%Y-%m-%d %H:%M:%S'
time_str = time.strftime(time_format, local_tuple)
print(time_str)
>>>
2019-03-16 15:14:35
time_tuple = time.strptime(time_str, time_format)
utc_now = time.mktime(time_tuple)
print(utc_now)
>>>
1552774475.0
```
Its behavior is determined by how the underlying C functions work with the host operating system.The time module fails to consistently work properly for multiple local times.
## datetime module
```python
from datetime import datetime, timezone
now = datetime(2019, 3, 16, 22, 14, 35)
now_utc = now.replace(tzinfo=timezone.utc)
now_local = now_utc.astimezone()
print(now_local)
>>>
2019-03-16 15:14:35-07:00
time_str = '2019-03-16 15:14:35'
now = datetime.strptime(time_str, time_format)
time_tuple = now.timetuple()
utc_now = time.mktime(time_tuple)
print(utc_now)
>>>
1552774475.0
```

>[!summary]
✦ Avoid using the time module for translating between different time
zones.
✦ Use the datetime built-in module along with the pytz community
module to reliably convert between times in different time zones.
✦ Always represent time in UTC and do conversions to local time as
the very final step before presentation.

# using the cppyreg modules
The copyreg module lets you register the functions responsible for serializing and deserializing Python objects, allowing you to control the behavior of pickle and make it more reliable.
## default attribute values
need implementation
