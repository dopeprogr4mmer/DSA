def infix_to_postfix(infix):
	def precedence(op):
		if op=='+' or op=='-':
			return 1
		elif op=='*' or op=='/':
			return 2
		elif op=='^':
			return 3
		else:
			return 0

	postfix = ''
	stack = ['#']
	for i in infix:
		if i.isalpha() or i.isnumeric():
			postfix+=i
			print(stack, postfix)
		elif i=='(':
			stack.append(i)
		elif i=='^':
			stack.append(i)
		elif i==')':
			while stack[-1]!='#' and stack[-1]!='(':
				postfix+=stack[-1]
				print(stack, postfix)
				stack.pop()
			stack.pop()
		else:
			#print(stack[-1])
			if precedence(i)>precedence(stack[-1]):
				stack.append(i)
			else:
				while stack[-1]!='#' and precedence(i)<=precedence(stack[-1]):
					postfix+=stack[-1]
					print(stack, postfix, i)
					stack.pop()
				stack.append(i)
	while stack[-1]!='#':
		postfix+=stack[-1]
		stack.pop()

	print(postfix)
	return postfix

infix_to_postfix('a+b*(c^d-e)^(f+g*h)-i')