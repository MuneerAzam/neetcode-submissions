# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def trav(node):
            if not node:
                return 0
            a=trav(node.right)
            b=trav(node.left)
            return 1+max(a,b)
        diameter=0
        def find(node):
            if not node:
                return
            nonlocal diameter
            a=trav(node.left)
            b=trav(node.right)
            diameter=max(diameter,(a+b))
            find(node.left)
            find(node.right)
        find(root)
        return diameter
