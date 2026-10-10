# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.flag=True
        def trav(node):
            if not node:
                return 0
            a=trav(node.left)
            b=trav(node.right)
            if abs(a-b)>1:
                self.flag=False
            return 1+max(a,b)
        trav(root)
        return self.flag
        