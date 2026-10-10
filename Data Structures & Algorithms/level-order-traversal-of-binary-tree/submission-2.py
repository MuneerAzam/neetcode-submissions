# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.d=defaultdict(list)
        def trav(node,level):
            if not node:
                return
            self.d[level].append(node.val)
            level+=1
            trav(node.left,level)
            trav(node.right,level)
        trav(root,0)
        return list(self.d.values())
        