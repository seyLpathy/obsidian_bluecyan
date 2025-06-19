from contextlib import contextmanager
import logging
@contextmanager
def debug_logging(level):
	logger=logging.getLogger()
	old_level=logger.getEffectiveLevel()
	logger.setLevel(level)
	try:
		yield 
		#Any exceptions that happen in the with block
        # will be re-raised by the yield expression for
		#  you to catch in the helper function
	finally:
		logger.setLevel(old_level)
def my_function():
	logging.debug("this is debug")
	logging.error('this is the error')
with debug_logging(logging.DEBUG):
	print('* Inside:')
	my_function()
print('* After:')
my_function()