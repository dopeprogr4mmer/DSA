class LinkedList:
<<<<<<< HEAD
<<<<<<< HEAD
	count = 0
	def __init__(self,value=None):
		self.value = value
		self.next = None
		LinkedList.count+=1
=======
	def __init__(self,value=None):
		self.value = value
		self.next = None
>>>>>>> d86366dc91ea42926b2be1e049e46fb03f518c05
=======
	def __init__(self,value=None):
		self.value = value
		self.next = None
>>>>>>> d86366dc91ea42926b2be1e049e46fb03f518c05

	def is_empty(self):
		if self.value == None:
			return True
		return False

	def append(self,value):
		if self.is_empty():
			self.value = value
			print('hi')
			return "no"

		if self.next == None:
			newnode = LinkedList(value)
			self.next = newnode
			print('done')
		else:
			self.next.append(value)
		return ()


	def insert(self,value,index):
		if index>self.get_length()-1:
			print("list index out of range")
			return ()
		if self.is_empty():
			self.append(value)
			return 'go'
		i = 0
		newnode = LinkedList(value)
		temp = self
		while i<index:
			temp = temp.next
			i+=1
		temp.value, newnode.value = newnode.value,temp.value
		newnode.next = temp.next
		temp.next = newnode


	def  delete(self,x):
		if self.is_empty():
			return()
		if self.value == x:
			self.value = None
<<<<<<< HEAD
<<<<<<< HEAD
			LinkedList.count-=1
=======
>>>>>>> d86366dc91ea42926b2be1e049e46fb03f518c05
=======
>>>>>>> d86366dc91ea42926b2be1e049e46fb03f518c05
			if self.next != None:
				self.value = self.next.value
				self.next = self.next.next
				return ()
		elif self.next != None:
			self.next.delete(x)
			if self.next.value == None:
				self.next = None
<<<<<<< HEAD
<<<<<<< HEAD
				LinkedList.count-=1
=======
>>>>>>> d86366dc91ea42926b2be1e049e46fb03f518c05
=======
>>>>>>> d86366dc91ea42926b2be1e049e46fb03f518c05
				return ()
		else:
			print('element not in list')


	def get_length(self):
		count = 1
		if self.is_empty():
			count = 0
			return 0

		temp = self

		while  temp.next != None:
			temp = temp.next
			count += 1

		assert count>0
		return count

<<<<<<< HEAD
<<<<<<< HEAD
	def reverse(self):
		k = LinkedList.count
		c = 0
		head = self
		prev_node, curr_node, next_node = None, head, None
		while curr_node and c<k:
			#print(curr_node.value)
			next_node = curr_node.next
			curr_node.next = prev_node
			prev_node = curr_node
			curr_node = next_node
			c+=1
		return prev_node

	def reverse_in_groups(self, k):
		c = 0
		head = self
		prev_node, curr_node, next_node = None, head, None
		while curr_node and c<k:
			#print(curr_node.value, c, k)
			next_node = curr_node.next
			curr_node.next = prev_node
			prev_node = curr_node
			curr_node = next_node
			c+=1
		if curr_node:
			head.next = curr_node.reverse_in_groups(k)
		return prev_node


=======
>>>>>>> d86366dc91ea42926b2be1e049e46fb03f518c05
=======
>>>>>>> d86366dc91ea42926b2be1e049e46fb03f518c05

	def  __str__(self):
		selflist = []

		if self.is_empty():
			return "Empty List"

		temp = self
		selflist.append(temp.value)
		while  temp.next != None:
			temp = temp.next
			selflist.append(temp.value)

		return(str(selflist))
		

l = LinkedList()
l.append(2)
print(l)
#l.append(5)
l.delete(1)
l.insert(10,0)
<<<<<<< HEAD
<<<<<<< HEAD
l.append(100)
l.append(42)
l.append(23)
l.append(7)
print(l)
#l.insert(11,0)
l.insert(102,0)
#l.delete(10)
print(l)
l.get_length()
#print(l.is_empty())
print(l.count)
head = l.reverse_in_groups(3)
print(head)
=======
=======
>>>>>>> d86366dc91ea42926b2be1e049e46fb03f518c05
print(l)
#l.insert(11,0)
l.insert(102,0)
l.delete(10)
print(l)
l.get_length()
<<<<<<< HEAD
#print(l.is_empty())
>>>>>>> d86366dc91ea42926b2be1e049e46fb03f518c05
=======
#print(l.is_empty())
>>>>>>> d86366dc91ea42926b2be1e049e46fb03f518c05
