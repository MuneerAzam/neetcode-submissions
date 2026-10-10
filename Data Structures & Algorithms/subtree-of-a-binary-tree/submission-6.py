# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.f=False
        def same(node):
            if not node:
                return
            def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
                flag=True
                def trav(node1,node2):
                    if not node1 and not node2:
                        return
                    nonlocal flag
                    if node1 and not node2 or node2 and not node1:
                        flag=False
                        return
                    if node1.val!=node2.val:
                        flag=False
                        return
                    trav(node1.left,node2.left)
                    trav(node1.right,node2.right)
                trav(p,q)
                return flag
            same(node.left)
            same(node.right)
            a=False
            if node.val==subRoot.val:
                a=isSameTree(node,subRoot)
            if a:
                self.f=True
                return
        same(root)
        return self.f      
