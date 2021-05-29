def braces(s,n):
	count = 0
	l = 0
	r = 0
	for i in range(n):
		if s[i] == '(':
			l+=1
		else:
			r+=1
		if l == r:
			x = l+r
			if x>count:
				count = x
		if r>l:
			l = r = 0
	l = r = 0

	for i in range(n-1, -1 ,-1):
		if s[i] == ')':
			r+=1
		else:
			l+=1
		if l == r:
			x = l+r
			if x>count:
				count = x
		if l>r:
			l = r = 0
	#print(count)
	print(count)

def alternate(s, n):
	stack = [-1]
	result = 0
	for i in range(n):
		if s[i]=='(':
			stack.append(i)
		else:
			if len(stack)!=0:
				#print(stack)
				stack.pop()
				result = max(result, i-stack[-1])
				#print(result, stack)
			else:
				stack.append(i)

	print(result)



alternate("((()()()()(((())",16)