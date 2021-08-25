<<<<<<< HEAD
<<<<<<< HEAD
from collections import deque, defaultdict
=======
>>>>>>> d86366dc91ea42926b2be1e049e46fb03f518c05
=======
>>>>>>> d86366dc91ea42926b2be1e049e46fb03f518c05
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

<<<<<<< HEAD
<<<<<<< HEAD



	def levelorder(self):
		q = deque()
		if self.is_empty():
			return []
		else:
			q.append(self)
		
		def lol(q, l=[]):
			if not q:
				#print(l)
				return l
			x = q.popleft()
			#print(x.value)
			l.append(x.value)
			if not x.left.is_empty():
				q.append(x.left)
			if not x.right.is_empty():
				q.append(x.right)
			return lol(q, l)
		return lol(q, [])

	def topview(self):
		q = deque()
		#tv[0]=self.value
		if self.is_empty():
			return []
		else:
			q.append((0, self))
		def view(q, tv={}):
			if not q:
				return tv
			x = q.popleft()
			index, node = x[0], x[1]
			if not index in tv.keys():
				tv[index]=node.value
				#print(tv)
			if not node.left.is_empty():
				q.append((index-1, node.left))
			if not node.right.is_empty():
				q.append((index+1, node.right))
			return view(q, tv)
		view_dict = view(q)
		#print(x)
		top_view = sorted(view_dict.items(), key=lambda x: x[0])
		#print(x)
		top_view = [i[1] for i in top_view]
		return top_view


	def bottomview(self):
		if self.is_empty():
			return []
		q = deque()
		q.append((0, self))
		def view(q, bv={}):
			"""If there are multiple bottom-most nodes 
			for a horizontal distance from root, 
			then print the later one in level traversal"""
			if not q:
				return bv
			z = q.popleft()
			index, node = z[0], z[1]
			#if not index in bv:			#diff bw top/bottom view
			bv[index] = node.value
			if not node.left.is_empty():
				q.append((index-1, node.left))
			if not node.right.is_empty():
				q.append((index+1, node.right))
			return view(q, bv)
		view_dict = view(q)
		bottom_view = sorted(view_dict.items(), key=lambda x: x[0])
		print(bottom_view)
		bottom_view = [i[1] for i in bottom_view]
		print(bottom_view)


	def verticalOrder(self): 
		if self == None:
		    return []
		output_list = []
		#i = 0
		q = [(0, self)]
		d = defaultdict(list)
		def sol(q, d):
		    if len(q)==0:
		        return d
		    z = q.pop(0)
		    d[z[0]].append(z[1].value)
		    if z[1].left!=None:
		        q.append((z[0]-1, z[1].left))
		    if z[1].right!=None:
		        q.append((z[0]+1, z[1].right))
		    return sol(q, d)
		
		vo = sol(q, d)
		if len(vo)!=0:
		    vo = sorted(vo.items(), key=lambda x: x[0])
		    op = [i[1] for i in vo]
		    for i in op:
		        output_list+=i
		    return output_list
		return []


	def leftview(self):
		if self.is_empty():
			return []
		depth, shift = 0, 0
		q = deque()
		q.append((depth, shift, self))
		def view(q, lv={}):
			#print(lv)
			if not q:
				return lv
			y = q.pop()
			depth, shift, node = y[0], y[1], y[2]
			if depth in lv.keys():
				if shift<lv[depth][0]:				#> for rightview
					lv[depth]=(shift, node.value)
			else:
				lv[depth]=(shift, node.value)
			if not node.left.is_empty():
				q.append((depth+1, shift-1, node.left))
			if not node.right.is_empty():
				q.append((depth+1, shift+1, node.right))
			return view(q, lv)
		view_dict = view(q)
		#print(view_dict)
		left_view = [view_dict[z] for z in view_dict]
		#print(left_view)
		left_view = [i[1] for i in left_view]
		return left_view

	def left_view_dfs(self, level=1, max_level=[0]):
		if self.is_empty():
			return 

		if max_level[0]<level:
			print(self.value)
			#return_list.append(self.value)
			max_level[0]=level

		self.left.left_view_dfs(level+1, max_level)
		self.right.left_view_dfs(level+1, max_level)


	def __str__(self):
		return str(self.topview())


	#print(dist)
	#return dist




#u = Tree()
#print(u.find(5))
t = Tree(100)
t.insert(50) 
t.insert(30)
t.insert(80)
t.insert(70)
t.insert(90)
t.insert(85)
t.insert(95)
#t.insert(1)
#print(t.delete(21))
#print(u.delete(2))
#print(t.preorder())
#print(t.postorder())
#print(t)
#print(t.topview())
#print(t.verticalOrder())
#print(t.left_view_dfs())
#distance(t, 30, 70)
#t.zigzag()
=======
=======
>>>>>>> d86366dc91ea42926b2be1e049e46fb03f518c05
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
<<<<<<< HEAD
print(t.postorder())
>>>>>>> d86366dc91ea42926b2be1e049e46fb03f518c05
=======
print(t.postorder())
>>>>>>> d86366dc91ea42926b2be1e049e46fb03f518c05
