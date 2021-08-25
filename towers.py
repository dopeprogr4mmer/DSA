def getMinDiff(self, arr, n, k):
    # code here
    arr.sort()
    #for i in range(n):
    #    arr[i]+=k
    min_, max_ = arr[0], arr[-1]
    ans = max_ - min_
    for i in range(1, n):
        if arr[i]>=k:
            max_, min_ = max(arr[i-1]+k, arr[-1]-k), min(arr[0]+k, arr[i]-k)
            ans = min(ans, max_-min_)
    
            
            
    #for i in range(n-1, -1, -1):
    #    arr[i] -= 2*k
    #    if arr[i]<0:
    #        break
    #    else:
    #        min_, max_ = min(arr[0], arr[i]), max(arr[i-1], arr[-1])
    #        #temp = max_ - min_
    #        ans = min(ans, max_ - min_)
    
    return ans