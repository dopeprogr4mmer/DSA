from collections import OrderedDict
from pprint import pprint 
class LRU:
	def  __init__(self, capacity):
		self.cache = OrderedDict()
		self.capacity = capacity

	def get(self, key):
		if not key in self.cache:
			print(-1)
			return -1
		self.cache.move_to_end(key)					#move to end of dict
		print(self.cache[key])
		return self.cache[key]

	def put(self, key, value):
		self.cache[key] = value
		self.cache.move_to_end(key)
		if len(self.cache)>self.capacity:
			self.cache.popitem(last=False)			#from beginning of dict

	def print_dict(self):
		pprint(self.cache)

class UsingDictionary:				#3.9<
	def __init__(self, capacity):
		self.cache = dict()
		self.capacity = capacity

	def get(self, key):
		if not key in self.cache:
			print(-1)
			return -1
		value = self.cache[key]
		self.cache.pop(key)			#remove key from dict
		self.cache[key] = value		#move to end of dict
		print(self.cache[key])
		return self.cache[key]

	def put(self, key, value):
		if key in self.cache:
			self.cache.pop(key)
		self.cache[key] = value
		#self.cache.move_to_end(key)
		if len(self.cache)>self.capacity:
			keys_view = self.cache.keys()
			key_iterator = iter(keys_view)
			first_key = next(key_iterator)
			self.cache.pop(first_key)			#from beginning of dict

	def print_dict(self):
		print(self.cache)						#doesnt work with pprint




od = UsingDictionary(5)
od.put(1,'Rahul')
od.put(3,'Phantom')
od.put(5,'aloha')
od.put(7,'Sionara')
od.put(-5,'zero')
od.print_dict()
od.put(6,'hi')
od.print_dict()
od.put(5,"jing")
od.print_dict()
od.get(2)
od.get(7)
od.print_dict()


"""
LRU
OrderedDict([(1, 'Rahul'),
             (3, 'Phantom'),
             (5, 'aloha'),
             (7, 'Sionara'),
             (-5, 'zero')])
OrderedDict([(3, 'Phantom'),
             (5, 'aloha'),
             (7, 'Sionara'),
             (-5, 'zero'),
             (6, 'hi')])
OrderedDict([(3, 'Phantom'),
             (7, 'Sionara'),
             (-5, 'zero'),
             (6, 'hi'),
             (5, 'jing')])
-1
Sionara
OrderedDict([(3, 'Phantom'),
             (-5, 'zero'),
             (6, 'hi'),
             (5, 'jing'),
             (7, 'Sionara')])
             """

"""
UsingDictionary
{-5: 'zero', 1: 'Rahul', 3: 'Phantom', 5: 'aloha', 7: 'Sionara'}
{-5: 'zero', 3: 'Phantom', 5: 'aloha', 6: 'hi', 7: 'Sionara'}
{-5: 'zero', 3: 'Phantom', 5: 'jing', 6: 'hi', 7: 'Sionara'}
-1
Sionara
{-5: 'zero', 3: 'Phantom', 5: 'jing', 6: 'hi', 7: 'Sionara'}
"""