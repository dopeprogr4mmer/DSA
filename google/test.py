from itertools import combinations
def test(s):
	l = []
	for i in range(1,len(s)+1):
	    x = list(combinations(s,i))
	    l += x
	
	l = ["".join(l[i]) for i in range(len(l))]
	l.sort()
	    
	return l

print(test('dmxn'))
