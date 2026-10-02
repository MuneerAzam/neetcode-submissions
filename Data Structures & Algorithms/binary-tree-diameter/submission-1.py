# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def trav(root):
            if not root:
                return 0
            a=trav(root.left)
            b=trav(root.right)
            return 1+max(a,b)
        def ans(root):
            if not root:
                return 0
            c=ans(root.left)
            d=ans(root.right)
            a=trav(root.left) if root.left is not None else 0
            b=trav(root.right) if root.right is not None else 0
            return max((a+b),c,d)
        return ans(root)