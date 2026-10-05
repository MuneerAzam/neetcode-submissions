# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level=defaultdict(int)
        def trav(node,l):
            if not node:
                return
            nonlocal level
            level[l]=node.val
            l+=1
            trav(node.left,l)
            trav(node.right,l)
        trav(root,0)
        return list(level.values())