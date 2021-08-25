class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

class Solution:
    sum_, carry, place = 0, 0, 1


    def get_length(self, l, length=0):
    	if not l:
    		return 0
    	length = 1
    	temp = l
    	while temp.next:
    		length+=1
    		temp = temp.next
    	return length
    
    def get_sum(self, l1, l2, r, z=0):
    	if not l1:
    		return 
    	self.get_sum(l1.next, l2.next, r.next, z+1)
    	global sum_
    	global carry
    	global place
    	total = l1.data + l2.data + Solution.carry
    	rem = total%10
    	Solution.carry = total//10
    	#print(carry) 
    	r.data = rem
    	Solution.sum_ = rem*Solution.place + Solution.sum_
    	Solution.place*=10
    	if z==0 and Solution.carry:
    		#print(Solution.carry)
    		doobie = Node(Solution.carry)
    		#print(doobie.data, Solution.place, Solution.sum_)
    		doobie.next = r
    		Solution.sum_ = Solution.place*Solution.carry + Solution.sum_
    		#print(Solution.sum_)
    		return doobie
    	#print(total, Solution.carry, rem, Solution.sum_)
    	return r
    	
    
    
    def addTwoLists(self, l1, l2):
    	if not l1 and not l2:
    		return -1
    	length1 = self.get_length(l1)
    	length2 = self.get_length(l2)
    	length = max(length1, length2)
    	#print(length1, length2)
    	#patch = 0b
    	if not length1==length2:
    		patch = Node(0)
    		if length==length1:
    			diff = length1 - length2
    			mellow = l2
    			flag = True
    		else:
    			diff = length2 - length1
    			mellow = l1
    			flag = False
    		while diff>0:
    			patch.next = Node(0)
    			patch = patch.next
    			diff-=1
    			if diff==0:
    				patch.next = mellow
    		if flag:
    			l2 = patch
    		else:
    			l1 = patch


    	result_list = Node(0)
    	t = result_list
    	while length>1:
    		#print(length)
    		t.next = Node(0)
    		t = t.next
    		length-=1
    
    	r = self.get_sum(l1, l2, result_list)
    	while r:
    		print(r.data)
    		r = r.next
    	return r
	

l1 = Node(6)
l1.next = Node(6) 
l1.next.next = Node(3)
l1.next.next.next = Node(7)
l2 = Node(9)
l2.next = Node(5)
l2.next.next = Node(4)
l2.next.next.next = Node(6)
l2.next.next.next.next = Node(0)

Solution().addTwoLists(l1, l2)
#get_number(None)
