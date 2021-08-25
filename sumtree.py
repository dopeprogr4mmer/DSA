# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def toSumTree(self, root) :
        #code here
        if not root:
            return 0
        if not (root.left or root.right):
            r = root.data
            root.data = 0
            return r
        z = root.data
        root.data = self.toSumTree(root.left) + self.toSumTree(root.right)
        return z + root.data