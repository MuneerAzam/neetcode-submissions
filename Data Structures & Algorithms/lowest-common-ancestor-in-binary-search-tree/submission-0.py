# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        visited={root:None}
        def trav(node):
            if not node:
                return 
            if node.left:
                visited[node.left]=node
            if node.right:
                visited[node.right]=node
            trav(node.left)
            trav(node.right)
        trav(root)
        node=p
        vis=set()
        while node:
            vis.add(node)
            node=visited[node]
        node=q
        while node not in vis:
            node=visited[node]
        return node