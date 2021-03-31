def is_rotation(str1,str2):
	if len(str1) != len(str2):
		return 0

	temp = str1+str1
	#print(temp)
	if temp.count(str2)>0:
		return 'Yes'
	return 'No'

what = is_rotation('AABB','BABA')
print(what)