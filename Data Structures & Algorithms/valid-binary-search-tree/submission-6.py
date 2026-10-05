# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        val=True
        def trav(node,mn,mx):
            if not node:
                return
            nonlocal val
            if node.val>=mx or node.val<=mn:
                val=False
                return
            trav(node.left,mn,node.val)
            trav(node.right,node.val,mx)
        trav(root,float("-inf"),float("+inf"))
        return val
        