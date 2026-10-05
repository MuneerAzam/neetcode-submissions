# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        val=True
        def trav(t1,t2):
            nonlocal val
            if not t1 and not t2:
                return
            if t1 and not t2:
                val=False
                return
            if not t1 and t2:
                val=False
                return
            if t1.val!=t2.val:
                val=False
            trav(t1.right,t2.right)
            trav(t1.left,t2.left)
        trav(p,q)
        return val