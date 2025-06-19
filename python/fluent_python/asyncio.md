## thread vs asyncio

### thread

![alt text](python/fluent_python/image-14.png)

### asyncio

![alt text](python/fluent_python/image-15.png)

### contrast

1. a task drives a coroutine and a thread invokes a callable
2. get _task_ objects by passing a coroutine to asyncio.async() or loop.create_task()
3. a task is already scheduled to run , a thread instance must be explicitly told to run by its start() method
4. thread use plain function and asyncio use coroutine
5. no API to terminate a thread from the outside,task can be terminated by task()
6. the supervisor coroutine must be executed with loop.run_until_complete() in the main function

## asyncio.Future:Nonblocking by Design

> [!keypoint]
> in asyncio, BaseEventLoop.create_task() takes a coroutine,schedules it to run, and returns an asyncio.Task instance.which is a subclass of Future designed to wrap a coroutine.

### result() method

1. asyncio.Future the .result() take no argument,if the future is not done,it doesn't block,it returns None.
2. in asyncio,yield from us used to give control back to the event loop
3. asynocio futures are driven by yield from,not by calling those methods

## yielding from Futures,Tasks and Coroutines

```python
res=yield from foo()
# note if foo is plain function ,res is a Future or Task instance
# note if foo is coroutine, res is coroutine object
```

### two ways of obtaining a Task

#### asyncio.async(coro_or_future,\*,loop=None)

if the first argument is a coroutine,it returns a Task instace An optional event loop may be passed as the loop= keyword argument; if omitted, async gets the loop object by calling asyncio.get_event_loop().

```python
>>> import asyncio
>>> def run_sync(coro_or_future):
... loop = asyncio.get_event_loop()
... return loop.run_until_complete(coro_or_future)
...
>>> a = run_sync(some_coroutine())
```

> [!summary]
> Every arrangement of coroutines chained with yield from must be ultimately driven by a caller that is not a coroutine, which invokes next(…) or .send(…) on the outermost delegating generator, explicitly or implicitly (e.g., in a for loop).The innermost subgenerator in the chain must be a simple generator that uses just yield—or an iterable object
![[Pasted image 20240623174229.png]]