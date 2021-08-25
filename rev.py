def rev(s):
	if len(s)%2!=0:
		return -1
	count = 0
	i, j = 1, 0
	l = list(s)
	if l[0]=='}':
	    l[0]='{'
	    count+=1
	if l[-1]=='{':
	    l[-1]='}'
	    count+=1
	for x in range(1,len(l)-1):
	    if l[x]=='{':
	        i+=1
	    else:
	        j+=1
	    #print(i,j,x)
	    if j>i:
	        l[x]='{'
	        count+=1
	        j-=1
	        i+=1
	    elif i-j>len(l)-1-x and l[x]=='{':
	        l[x]='}'
	        count+=1
	    #print(i,j,l,count)
	print(count)


rev('}}}}}}{}{}}}{{}}}}{}}{{{}{}{}{}}{{{{}}}{}}')