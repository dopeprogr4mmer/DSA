import heapq

arr = [2, 4, 1, 9, 5]
k = [2,6,1,7,0,9,3]
heapq.heapify(k)						#heapify array in place, in linear time
print(k)
#nsorted(arr)
h = []
z = [11, 8, 0, 6]
for i in arr:
	heapq.heappush(h, i)
print(h)
x = heapq.heappop(h)
print(x, h)
for j in z:
	y = heapq.heapreplace(h, j)    #pop then push
	#y = heapq.heappushpop(h, j)     #push then pop
	print(y, h)

a = [1,5,9,13,17]
b = [0,2,4,6,8]
c = [3,7,11,15,19]

z = heapq.merge(a, b, c)#Merge multiple sorted inputs into a single sorted output
#heapq.merge(*iterables, key=None, reverse=False) 

print(list(z))

m = heapq.nlargest(3, arr)		#heapq.nlargest(*iterables, key=None)
#Equivalent to: sorted(iterable, key=key, reverse=True)[:n]

n = heapq.nsmallest(3, arr)[:3]	#heapq.nsmallest(*iterables, key=None)
#Equivalent to: sorted(iterable, key=key)[:n]
print(m, n)

class Node:
    def __init__(self,x):
        self.data = x
        self.nxt = None

def nsortedarr(matrix):
	l = arr[0]
	length = len(arr)
	for i in range(1, length):
		l = list(heapq.merge(l, arr[i]))
	return l


def nsortedll(ll):
	save = []
	for i in ll:
		queue = i 
		while queue:
			heapq.heappush(save, queue.data)
			queue = queue.nxt

	#print(save)
	head = Node(heapq.heappop(save))
	temp = head

	while len(save)!=0:
		temp.nxt = Node(heapq.heappop(save))
		temp = temp.nxt	

	while head!=None:
		print(head.data)
		head = head.nxt 


i = Node(1)
i.nxt = Node(2)
i.nxt.nxt = Node(3)
j = Node(2)
j.nxt = Node(4)
j.nxt.nxt = Node(5)
k = Node(2)
k.nxt = Node(5)
k.nxt.nxt = Node(6)
l = Node(2)
l.nxt = Node(7)
l.nxt.nxt = Node(8)
nsortedll([i,j,k,l])

def heapify(arr, i, n):
	#n = len(arr)
	smallest = i 
	l = i*2 + 1
	r = i*2 + 2

	if l<n and arr[l]<arr[smallest]:
		smallest = l 

	if r<n and arr[r]<arr[smallest]:
		smallest = r 

	if smallest!=i:
		arr[i], arr[smallest] = arr[smallest], arr[i]
		heapify(arr, smallest, n)

def heappop(heap):
	z = heap.pop(0)
	heapify(heap, 0, len(heap))
	return z

def heappush(arr, element):
	#print(arr)
	arr.insert(0, element)
	#print(arr)
	heapify(arr, 0, len(arr))

def merge(matrix):
	save = matrix[0]
	for i in range(1,len(matrix)):
		for element in matrix[i]:
			heappush(save, element)

	print(save)
	n = len(save)
	for i in range(n-1, -1, -1):
		save[0], save[i] = save[i], save[0]
		heapify(save, 0, i)

	print(save)




arx = [1, 2, 9]
heappush(arx, 3)
print(arx)
print(heappop(arx))
print(arx)
merge([[1,2,5],[3,4,7],[0,5,8]])


