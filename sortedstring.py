class alphanumeric:
    def __init__(self,name,count):
        self.name=name
        self.count=count
        
class Solution:
    def sortedStrings(A):
        #code here
        B = list(set(A))
        B.sort()
        output = [alphanumeric(string, A.count(string)) for string in B]
        return output

A = ["2234597891 zmxvvxbcij 8800654113 jihgfedcba",
"1234567891 zxyabcvapo 0123434908 padmadngaa",
"1234567891 abcdefghij 9876543219 jihgfedcba",
"2234597891 zmxvvxbcij 8800654113 jihgfedcba",
"9120121291 zmxvvxbcij 0912114113 mnvxbedcba"]

Solution.sortedStrings(A)