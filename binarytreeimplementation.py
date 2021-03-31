class Tree:
	def __init__(self,value = None):
		self.value = value
		if self.value:
			self.left = Tree()
			self.right = Tree()
		else:
			self.left = None
			self.right = None
		return 

	def is_empty(self):
		return (self.value == None)

	def is_leaf(self):
		return (self.right.is_empty() and self.left.is_empty())

	def min_val(self):
		if self.left.is_empty():
			return self.value
		return self.left.min_val()

	def max_val(self):
		if self.right.is_empty():
			return self.value
		else:
			return self.right.max_val()


	def find(self,x):
		if self.is_empty():
			return False
		if self.value == x:
			return True
		if x<self.value:
			return self.left.find(x)
		else:
			return self.right.find(x)

	def insert(self,x):
		if self.is_empty():
			self.value = x
			self.left = Tree()
			self.right = Tree()
		if self.value == x:
			return "Element already present"
		if x<self.value:
			self.left.insert(x)
			return
		if x>self.value:
			self.right.insert(x)
			return

	def make_empty(self):
		self.value = None
		self.left = None
		self.right = None
		return

	def  copy_right(self):
		self.value = self.right.value
		self.left = self.right.left
		self.right = self.right.right

	def delete(self,x):
		if self.is_empty():
			return "Empty Tree"
		if not self.find(x):
			return "Element not in Tree"
		if x<self.value:
			self.left.delete(x)
			return
		if x>self.value:
			self.right.delete(x)
			return
		if x == self.value:
			if self.is_leaf():
				self.make_empty()
			elif self.left.is_empty():
				self.copy_right()
			else: 
				self.value = self.left.max_val()
				self.left.delete(self.left.max_val())
		

	def inorder(self):
		if self.is_empty():
			return []
		else:
			return (self.left.inorder() + [self.value] + self.right.inorder())

	def preorder(self):
		if self.is_empty():
			return []
		else:
			return ([self.value] + self.left.preorder() + self.right.preorder())

	def postorder(self):
		if self.is_empty():
			return []
		else:
			return (self.left.postorder() + self.right.postorder() +[self.value])

	def __str__(self):
		return str(self.inorder())


u = Tree()
print(u.find(5))
t = Tree(7)
t.insert(2)
t.insert(4)
t.insert(5)
t.insert(3)
t.insert(11)
t.insert(8)
print(t.delete(21))
print(u.delete(2))
print(t.inorder())
print(t.preorder())
print(t.postorder())