class Node(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def in_order(root):
	if not root:
		return []
	return in_order(root.left) + [root.val] + in_order(root.right)

def pre_order(root):
	if not root:
		return 
	curr = root
	stack = [curr]
	while len(stack)>0:
		z = stack.pop()
		print(z.val, end=" ")
		if z.right:
			stack.append(z.right)
		if z.left:
			stack.append(z.left)


def sort_array(arr):
	swap = 0
	i = 0
	while True:
		if i >= len(arr):
			break
		z = arr.index(min(arr[i:]))
		if z>i:
			arr[i], arr[z] = arr[z], arr[i]
			swap+=1
		i+=1

	print(arr)
	return swap, arr

def bt_to_bst(root, arr):
	if not root:
		return
	bt_to_bst(root.left, arr)
	root.val = arr[0]
	#print(root.val)
	arr.pop(0)
	bt_to_bst(root.right, arr)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
#root.left.right.left = Node(7)
#root.left.right.right = Node(8)
#root.left.right.right.right = Node(9)
root.right.left = Node(6)
root.right.left = Node(7)
inorder = in_order(root)
print(inorder)
min_swap, arr = sort_array(inorder)
print(min_swap)
bt_to_bst(root, arr)
print(in_order(root))
pre_order(root)