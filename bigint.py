def modulo_multiplication(a, b, m):
	res = 0
	#a = a%m
	while b:
		if b&1:
			res += a
			b -= 1
			res%=m
		if b:
			a *= 2
			a%=m
			#res += a
		b = b>>1
		print(res, a, b)

	print(res)
	return res

modulo_multiplication(10123465234878998, 65746311545646431, 10005412336548794)

#print((10123465234878998*65746311545646431)%10005412336548794)