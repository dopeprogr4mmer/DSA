def four_elements(arr, n, X):
	d = {}
	for i in range(n-1):
		for j in range(i+1, n):
			d[arr[i]+arr[j]] = [i, j]
	
	for i in range(n-1):
		for j in range(i+1, n):
			sum_ = X - (arr[i]+arr[j])
			if sum_ in d:
				y = d[sum_]
				if not(y[0]==i or y[1]==j or y[1]==j or y[0]==i):
					return [arr[i], arr[j], arr[y[0]], arr[y[1]]]
		return False



if __name__ == '__main__':
	try:
		arr = [10, 20, 30, 40, 1, 2]
		X = 91
		elements=four_elements(arr, len(arr), 91)
		if elements:
			print(elements)
		else:
			print("No such elements found!")
	except Exception:
		errorno = 50159747054
		print(f"Hey Phantom, there's a {errorno: #x} error")