from datetime import datetime, timedelta

class NewBucket:
	def __init__(self,period):
		self.period_delta=timedelta(seconds=period)
		self.reset_time=datetime.now()
		self.quota_consumed=0
		self.max_quota=0
	def __repr__(self) -> str:
		return (f'NewBucket(max_quota={self.max_quota},'
		  		f'quota_consumed={self.quota_consumed})')
	@property
	def quota(self):
		return self.max_quota -self.quota_consumed
	@quota.setter
	def quota(self,amount):
		delta=self.max_quota-amount	
		if amount==0:
			# being reset
			self.quota_consumed=0
			self.max_quota=0
		elif delta<0:
			assert self.quota_consumed==0
			self.max_quota=amount
		else:
			assert self.max_quota>=self.quota_consumed
			self.quota_consumed+=delta


def fill(bucket, amount):
	now = datetime.now()
	if (now - bucket.reset_time) > bucket.period_delta:
		bucket.quota = 0
		bucket.reset_time = now
	bucket.quota += amount

def deduct(bucket, amount):
	now = datetime.now()
	if (now - bucket.reset_time) > bucket.period_delta:
		return False # Bucket hasn't been filled this period
	if bucket.quota - amount < 0:
		return False # Bucket was filled, but not enough