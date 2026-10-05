# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        val=True
        change=False
        def same(t1,t2):
            nonlocal val
            if not t1 and not t2:
                return
            if t1 and not t2:
                val=False
                return
            if not t1 and t2:
                val=False
                return
            if t1.val!=t2.val:
                val=False
            same(t1.right,t2.right)
            same(t1.left,t2.left)
        def trav(node):
            if not node:
                return 
            if node.val==subRoot.val:
                nonlocal val
                nonlocal change
                change=True
                val=True
                same(node,subRoot)
                if change and val:
                    return True
            trav(node.left)
            trav(node.right)
        trav(root)
        if change:
            return val
        else:
            return change