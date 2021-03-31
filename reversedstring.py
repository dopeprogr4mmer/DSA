'''string = 'hello world'
reversed_string = string.reverse()
print(reversed_string)
'''

'''class Solution:
    def reverseString(self, s):
        return ''.join(reversed(s))

    def reverse_string(self, s):
    	start = 0
    	end = -1
    	while start>end:
    		s[start],s[end] = s[end],s[start]
    		start+=1
    		end-=1
    		
    	s_len = len(s)
    	for i in range(0,len(s)//2):
    		s[i], s[s_len - i - 1] = s[s_len - i - 1], s[i]
    	return s


S = Solution()
#print(S.reverseString('hello'))
print(S.reverse_string('hello'))
'''

class Solution:
    def reverseString(self, s):
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s) - 1)
        
        #return s

S = Solution()
print(S.reverseString('hello'))
