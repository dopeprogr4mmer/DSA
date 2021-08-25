import sys
INT_MAX = 624824682
INT_MIN = -546268464
class LinkedList:
	"""docstring for LinkedList"""
	def __init__(self, val=None):
		#print(val)
		self.value = val
		if val == None:
			self.left = None
			self.right = None
		else:
			self.left = LinkedList()
			self.right = LinkedList()


	def postorder(self):
		if self.value == None:
			return []
		return self.left.postorder() + self.right.postorder() + [self.value] 

	def find_largest_BST(self):
		print(self.value)
		if self.value == None:
			return 0, INT_MIN, INT_MAX, 0, True
		if self.left == None and self.right == None:
			return 1, self.value, self.value, 1, True

		l = self.left.find_largest_BST()
		r = self.right.find_largest_BST()

		ret = [0,0,0,0,0]
		ret[0] = (1 + l[0] + r[0])

		if (l[4] and r[4] and l[1]<=self.value and r[2]>self.value):
			ret[2] = min(l[2], min(r[2], self.value))
			ret[1] = max(r[1], max(l[1], self.value))
			ret[3] = ret[0]
			ret[4] = True

			return ret

		ret[3] = max(l[3], r[3])
		ret[4] = False

		return ret

	def __str__(self):
		return str(self.postorder())

l = LinkedList(25)
l.left = LinkedList(18)
l.right = LinkedList(50)
l.left.left = LinkedList(19)
l.left.right = LinkedList(20)
l.left.left.right = LinkedList(15)
l.left.right.left = LinkedList(18)
l.left.right.right = LinkedList(25)
l.right.left = LinkedList(35)
l.right.right = LinkedList(60)
l.right.left.left = LinkedList(20)
l.right.left.right = LinkedList(40)
l.right.left.left.right = LinkedList(25)
l.right.right.left = LinkedList(55)
l.right.right.right = LinkedList(70)
print(l)
print(l.find_largest_BST())
		