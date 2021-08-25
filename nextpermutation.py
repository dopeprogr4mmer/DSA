class Solution(object):
    def nextPermutation(self, nums):
<<<<<<< HEAD
<<<<<<< HEAD
        """
        Not in place
        """
        N = len(nums)
        k = 0
        for i in range(N-1, -1, -1):
            if nums[i-1]<nums[i]:
                k = i-1
                break
        if k == -1:
            return nums[::-1]
        z = 0
        for j in range(k+1, N):
            if nums[j]>nums[k]:
                z = j
        nums[k], nums[z] = nums[z], nums[k]
        nums = nums[:k+1]+list(reversed(nums[k+1:]))
        return nums

    def nextPermutationInPlace(self, nums):		
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k = 0
        for i in range(N-1, -1, -1):
            if nums[i-1]<nums[i]:
                k = i-1
                break
        if k == -1:
            i = 0
            j = N-1
            while(i<j):
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j-=1
            #nums = nums[::-1]
            #return nums
        else:
            z = 0
            for j in range(k+1, N):
                if nums[j]>nums[k]:
                    z = j
            nums[k], nums[z] = nums[z], nums[k]
            i = k+1
            j = N-1
            while(i<j):
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j-=1
        return nums


solution = Solution()
sol = solution.nextPermutationInPlace([3, 2, 1])
=======
=======
>>>>>>> d86366dc91ea42926b2be1e049e46fb03f518c05
        for i in range(len(nums)-1,-1,-1):
        	for j in range(i-1,-1,-1):
        		if nums[i]>nums[j]:
        			nums[i], nums[j] = nums[j], nums[i]
        			return nums
        return(sorted(nums))


solution = Solution()
sol = solution.nextPermutation([5,4,3,2,1])
<<<<<<< HEAD
>>>>>>> d86366dc91ea42926b2be1e049e46fb03f518c05
=======
>>>>>>> d86366dc91ea42926b2be1e049e46fb03f518c05
print(sol)
        