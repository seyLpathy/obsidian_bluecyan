## basic behavior

### four stages of a coroutines

![[Pasted image 20240621140257.png]]

1. GEN_CREATED
2. GEN_RUNNING
3. GEN_SUSPENDED(.send() works at this stage) the execution of the coroutine is suspended exactly at the yield keyword
4. GEN_CLOSED
   ![[Pasted image 20240621140638.png]]

## running average

![[Pasted image 20240621141420.png]]

![[Pasted image 20240621141437.png]]

> [!keypoint]
> the keyword ==yield== will suspend the corountines and wait for the next calling
> so first you send you must need use next to activate

## decorator for coroutine priming

```python
from coroutil import coroutine
@coroutine # prime the corountine
def averager():
	total = 0.0
	count = 0
	average = None
	while True:
		term = yield average
		total += term
		count += 1
		average = total/count
```

## exception_handle

1. if exception not handle ,the coroutines will terminate,any attempt to reactivate it will raise stopiteration
2. if an unhandled exception is thrown into the coroutine, it stops its state becomes 'GEN_CLOSED
   ![[Pasted image 20240621142921.png]]

## return value

> [!keypoint]
> must terminate a coroutines before retrive the data

```python
try:
	... coro_avg.send(None)
... except StopIteration as exc:
	... result = exc.value
```

## yield from

the basic: yield from the iterable
![[Pasted image 20240621143755.png]]
• Each iteration of the outer for loop creates a new grouper instance named group;
this is the delegating generator.
• The call next(group) primes the grouper delegating generator, which enters its
while True loop and suspends at the yield from, after calling the subgenerator
averager.
• The inner for loop calls group.send(value); this feeds the subgenerator averag
er directly. Meanwhile, the current group instance of grouper is suspended at the
yield from.
• When the inner for loop ends, the group instance is still suspended at the yield
from, so the assignment to results[key] in the body of grouper has not happened
yet.
• Without the last group.send(None) in the outer for loop, the averager subgeneratornever terminates, the delegating generator group is never reactivated, and the assignment to results[key] never happens.
• When execution loops back to the top of the outer for loop, a new grouper instanceis created and bound to group. The previous grouper instance is garbage collected(together with its own unfinished averager subgenerator instance).

### example

```python
_i = iter(EXPR)
try:
	_y = next(_i)
except StopIteration as _e:
	_r = _e.value
else:
	while 1:
		_s = yield _y
	try:
	_y = _i.send(_s)
	except StopIteration as _e:
	_r = _e.value
	break
RESULT = _r
```

### case:discreate event simulation

#### the coroutine

1. event("event","time proc action")#具体的事件(时间，实例的 id,行为描述)
2. taxi_process(ident,trips,start_time) work as a coroutine(构建目标物，一个 generator 模拟行为)
3. main()主程序通过 send()方法激活 coroutine
4. final event 结束后 raise stopiteration
5. 事件模拟完毕

#### the simulator.run

![alt text](python/fluent_python/image-10.png)
![alt text](python/fluent_python/image-11.png)
