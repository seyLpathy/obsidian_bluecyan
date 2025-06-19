from functools import wraps
def trace_func(func):
	if hasattr(func,'tracing'):
		return func
	
	@wraps(func)
	def wrapper(*args,**kwargs):
		result=None
		try:
			result=func(*args,**kwargs)
			return result
		except Exception as e:
			result=e
			raise
		finally:
			print(f'{func.__name__}({args!r},{kwargs!r})->'
							f'{result!r}')
			wrapper.tracing=True
			return wrapper
	