def assert_example(n):
	n -= n*(0.10)
	assert 0<n<10	
	return n		#internal selfcheck for the program

n = assert_example(100)
print(n)