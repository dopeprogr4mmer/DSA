class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

def print_ll(head):
	temp = head
	while True:
		if not temp:
			break
		print(temp.val, end=" ")
		temp = temp.next

def reverse(curr, prev=None):
	if not curr:
		return prev
	next_ = curr.next
	curr.next = prev
	return reverse(next_, curr)

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
print_ll(head)
new_head = reverse(head)
print()
print_ll(new_head)

