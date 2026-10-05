# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level=defaultdict(list)
        def trav(node,l):
            if not node:
                return
            nonlocal level
            level[l].append(node.val)
            l+=1
            trav(node.left,l)
            trav(node.right,l)
        trav(root,0)
        return list(level.values())