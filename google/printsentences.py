def do_little(arr, m, n, output):
	#print(m,n,output)
	output[m] = arr[m][n]
	if m==len(arr)-1:
		print(" ".join(output))
		return
	for i in range(len(arr[0])):
		if arr[m+1][i]!="":
			do_little(arr, m+1, i, output)


def combine(arr, r, c):
	output = [""]*r
	#print(output)
	for i in range(c):
		if arr[0][i]!="":
			do_little(arr, 0, i, output)


def alternate(arr, r, c):			#Works! :-)
	def do_little(arr, m, n, output):
		#print(m,n,output)
		output[m] = arr[m][n]
		if m==len(arr)-1:
			print(" ".join(output))
			return
		for i in range(len(arr[0])):
			if arr[m+1][i]!="":
				do_little(arr, m+1, i, output)
	output = [""]*r
	#print(output)
	for i in range(c):
		if arr[0][i]!="":
			do_little(arr, 0, i, output)


arr = [["you", "we", "they", ""],
       ["have", "are", "will", ""],
       ["sleep", "eat", "drink", "play"],
       ["dear", "bear", "good", "bye"],
       ["1", "2", "3", "4"],
       ["o", "l", "a", "y"]]


combine(arr, len(arr), len(arr[0]))
#alternate(arr, len(arr), len(arr[0]))