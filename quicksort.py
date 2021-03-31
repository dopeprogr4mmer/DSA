from sys import setrecursionlimit
#from past.builtins import xrange
setrecursionlimit(10000000)
from random import shuffle
def quicksort(Array,left,right):
	if right-left <= 1:
		return ()
	yellow = left+1
	for green in range(left+1,right):
		if Array[green]<=Array[left]:
			Array[yellow],Array[green] = Array[green],Array[yellow]
			yellow+=1
	Array[left],Array[yellow-1] = Array[yellow-1],Array[left]
	quicksort(Array,left,yellow-1)
	quicksort(Array,yellow,right)
	return Array

Array = [x for x in range(10000)]
shuffle(Array)
#print(Array)
#print(Array)
sorted_array = quicksort(Array,0,len(Array))
print(sorted_array)
