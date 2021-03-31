class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
	def minimumPlatform(self,n,arr,dep):
		max_count = 1
		count = 1
		i = 0
		while(i<len(arr)-1):
			for j in range(i+1,len(arr)):
				if dep[j]<=dep[i] or arr[j]<=arr[i]:
					count+=1
				else:
					if count>max_count:
						max_count = count
						count = 1
					i = j
					break

		print(max_count)


arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

solution = Solution()
solution.minimumPlatform(6, arr, dep)