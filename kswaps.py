def kswaps(s, k):
	global max_s
	if int(s)>int(max_s):
		max_s = s
	if k <= 0:
		#print(max_s)
		return
	a = list(s)
	#maximum = int(s)
	for i in range(len(a)-1):
		for j in range(len(a)):
			if a[j]>a[i]:
				a[i], a[j] = a[j], a[i]
				z = "".join(a)
				kswaps(z, k-1)
				a[i], a[j] = a[j], a[i]
	#print(max_s, "k")
	#print(max_s)
	return max_s




max_s = "0"

print(kswaps("129814999", 4))

#print(max_s)