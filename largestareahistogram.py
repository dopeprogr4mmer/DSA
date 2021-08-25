class Solution:
    def largest_area_histogram(self, histogram):
        stack = []
        index = 0
        max_area = 0
        
        def get_area(stack, histogram, index):
            top_of_stack = stack.pop()
            bar_area = histogram[top_of_stack]
            if len(stack)>0:
                area = bar_area*(index - stack[-1] - 1)
            else:
                area = bar_area*index
            return area
    
        while index<len(histogram):
            if len(stack)==0 or histogram[stack[-1]]<=histogram[index]:
                stack.append(index)
                index+=1
            else: 
                area = get_area(stack, histogram, index)
                max_area = max(area, max_area)
        while len(stack)>0:
            area = get_area(stack, histogram, index)
            max_area = max(area, max_area)
        
        #print(max_area)
        return max_area
        
    def maxArea(self,M, m, n):
        # code here
        max_area = 0
        for i in range(m):
            if i == 0:
                max_area = self.largest_area_histogram(M[i])
                continue
            for j in range(n):
                if M[i][j]!=0:
                    M[i][j] += M[i-1][j]
            area = self.largest_area_histogram(M[i])
            print(area)
            max_area = max(area, max_area)
        #print(max_area)
        return max_area
#{ 
#  Driver Code Starts
#Initial Template for Python 3



# Driver Code 
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        R,C = map(int, input().strip().split())
        A = []
        for i in range(R):
            line = [int(x) for x in input().strip().split()]
            A.append(line)
        print(Solution().maxArea(A, R, C)) 
    
# This code is contributed 
# by SHUBHAMSINGH10 

# } Driver Code Ends