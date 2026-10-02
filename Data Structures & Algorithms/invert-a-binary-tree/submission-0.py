# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def trav(node):
            if not node:
                return
            t=node.left
            node.left=node.right
            node.right=t
            trav(node.left)
            trav(node.right)
        trav(root)
        return root