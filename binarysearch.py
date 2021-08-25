import sys
sys.setrecursionlimit(100000)
def binary_search(sequence,value,left,right):
	if (right-left) == 0:
		return False
	mid = (right+left)//2
	#bprint(mid,sequence[mid],left,right)
	if (value == sequence[mid]):
		return sequence.index(value),sequence[mid]
	if (value<sequence[mid]):
		return binary_search(sequence,value,left,mid)
	if (value>sequence[mid]):
		return binary_search(sequence,value,mid+1,right)
#print(1//2,'j')
print(binary_search([16,22,23,24,33,40,41,42,44],42,0,9))
#print(1//2)