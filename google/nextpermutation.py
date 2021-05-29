def nextPermutation(N, arr):
    # code here
    #print(arr)
    k = 0
    for i in range(N-1, -1,-1):
        if arr[i]>arr[i-1]:
            #print(arr[i],arr[i-1])
            k = i-1
            break
    if k==-1:
        #print('s')
        return list(reversed(arr))
        
    z = 0
    for j in range(k+1,N):
        if arr[j]>arr[k]:
            z = j
    #print(k,z)
            
    arr[z], arr[k] = arr[k], arr[z]
    #print(arr[:k+1], list(reversed(arr[k+1:])))
    arr = arr[:k+1]+list(reversed(arr[k+1:]))
    #print(arr)
    return arr


print(nextPermutation(4, [1,4,3,2]))