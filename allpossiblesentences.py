def all_possible_sentences():
	pass

all_possible_sentences()

def searchMatrix(matrix, target):
    for i in range(len(matrix)):
    	#print(matrix[i])
    	for j in range(len(matrix[i])):
        	#print(matrix[i][j])
        	if matrix[i][j] == target:
        		#print(matrix[i][j])
        		#print((matrix.index(target)))
        		return True
    return False

c = searchMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]],3)
print(c)

