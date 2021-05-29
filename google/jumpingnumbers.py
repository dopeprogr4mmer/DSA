class Queue:
	def __init__(self):
		self.q = []

	def not_empty(self):
		if self.q == []:
			return False
		return True

	def enque(self, value):
		#print('jghg')
		self.q.append(value)

	def deque(self):
		return self.q.pop(0)


def bfs(x, num):
	#print(x, "hi")
	output = []
	queue = Queue()
	#print('j', queue)
	queue.enque(num)

	#print('k')

	while (queue.not_empty()):
		num = queue.deque()

		if num<x:
			#print(str(num), end = " ")
			output.append(num)
			ld = num%10

			if ld == 0:
				queue.enque(num*10 + (ld+1))

			elif ld == 9:
				queue.enque(num*10 + (ld-1))

			else:
				queue.enque(num*10 + (ld+1))
				queue.enque(num*10 + (ld-1))
	#print(output)

	return output

def jumper(x):
	output = []
	for i in range(10):
		output += [i]
		output += bfs(x, i)
	output = list(set(output))
	return output



if __name__ == '__main__':
	try:
		string = "1??0?101"
		x = int(input("Enter range:"))
		#print(x)
		output = jumper(x)
		if output!=[]:
			output.sort()
			for number in output:
				print(number, end=" ")
		else:
			print("No such number found!")
	except Exception:
		errorno = 50159747054
		print(f"Hey Phantom, there's a {errorno: #x} error")