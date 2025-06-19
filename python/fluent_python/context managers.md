## else blocks beyond if 
1. for else else block will run only if and when the for loop runs to completion
2. The else block will run only if and when the while loop exits because the condition became falsy
3. The else block will only run if no exception is raised in the try block
```python
for item in my_list:
	if item.flavor == 'banana':
		break
else:
	raise ValueError('No banana flavor found!')


try:
	dangerous_call()
except OSError:
	log('OSError...')
else:
	after_call()
```

## with blocks
### context manager 
	1.\_\_enter\_\_   which return the some other object or context manager
	2. \_\_exit\_\_   exit the with block control 

```python
>>> from mirror import LookingGlass
>>> with LookingGlass() as what:
	... print('Alice, Kitty and Snowdrop')
	... print(what)
	...
pordwonS dna yttiK ,ecilA
YKCOWREBBAJ
>>> what
'JABBERWOCKY'
>>> print('Back to normal.')
Back to normal.
```

![[Pasted image 20240621134325.png]]

## the context utilities
1. closing
2. suppress
3. ==@contextmanager==
4. ContextDecorator
5. ExitStack
### @contextmanager
1. everything before the yield will be executed when __enter__  called
2. the code after yield will be excuted when __exit__ called 
