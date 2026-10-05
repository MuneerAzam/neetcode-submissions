# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        lst=[]
        def trav(node,idx):
            if not node:
                return 
            nonlocal lst
            trav(node.left,idx)
            lst.append(node.val)
            trav(node.right,idx)
        trav(root,0)
        return lst[k-1]