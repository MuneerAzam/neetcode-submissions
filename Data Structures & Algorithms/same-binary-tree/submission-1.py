# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.flag=True
        def trav(node1,node2):
            if not node1 and not node2:
                return
            if node1 and not node2 or node2 and not node1:
                self.flag=False
                return
            if node1.val!=node2.val:
                self.flag=False
                return
            trav(node1.left,node2.left)
            trav(node1.right,node2.right)
        trav(p,q)
        return self.flag
