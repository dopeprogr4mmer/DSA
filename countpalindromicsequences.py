def count_palindromic_sequences(string):
	count = 0
	for i in range(len(string)):
		for j in range(i,len(string)):
			temp_string = string[i:j+1]
			print(i,j,temp_string)
			if temp_string == ''.join(reversed(temp_string)):
				print('hi')
				count+=1

	return count

#count = count_palindromic_sequences('aaaa')
#print(count)

'''
A = [[1,2,3,4],[5,6,8,9],[7,11,25,32],[85,96,74,19]]
m = len(A)
n = len(A[0])
count = 0
for i in range(m):
	for j in range(n):
		count+=1
		print(count)
		'''

def permutation(string):
	if len(string)==0:
		return ''
	if len(string)==1:
		return string
	l = []
	for i in range(len(string)):
		m = string[i]
		p = string[:i]+string[i+1:]
		print(p)
		for x in permutation(p):
			l.append(m+x)

	print(l)



permutation('abcde')