class Solution(object):
    def nextPermutation(self, nums):
        for i in range(len(nums)-1,-1,-1):
        	for j in range(i-1,-1,-1):
        		if nums[i]>nums[j]:
        			nums[i], nums[j] = nums[j], nums[i]
        			return nums
        return(sorted(nums))


solution = Solution()
sol = solution.nextPermutation([5,4,3,2,1])
print(sol)
        