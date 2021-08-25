import sys
#import numpy as np
class Solution:				#didn't quite understand but it works
    def median(self, matrix, r, c):
        #code here
        x = np.array(matrix)
        y=np.ravel(x)
        z = sorted(y)
        left = 0
        right = len(z)-1
        mid = (left + (right-left))//2
        return(z[mid])


def sol(matrix, r, c):
	#code here
    a = []
    for i in range(r):
        a+=matrix[i]
    a.sort()
    index = (r*c)//2
    print(a, index)
    return a[index]

M = [[1, 3, 5], 
     [2, 6, 9], 
     [3, 6, 9]]

sol(M,3,3)