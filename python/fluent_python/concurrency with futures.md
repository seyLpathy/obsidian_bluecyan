## example
### the sequence dowhloader
![alt text](python/fluent_python/image-12.png)
### the concurrent.future
![alt text](python/fluent_python/image-13.png)
## the Future 
1. concurrent.future.Future
2. asyncio.Future
>[!definition]
> an instance of either Future class represnts a deferred computaiton that 
> may or may not have completed

3. they are meant to instantiated exclusively the concurrency framework 
## launching with concurrent.futures
processpoolexcutor(default=os.cpu_count())
Python processes using the ProcessPoolExecutor class—thus bypassing the GIL and leveraging all available CPU cores, if you need to do CPU-bound processing.
## experimentin with Executor.map



