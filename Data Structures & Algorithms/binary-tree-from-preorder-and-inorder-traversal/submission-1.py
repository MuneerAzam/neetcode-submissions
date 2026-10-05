# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pos = {val: i for i, val in enumerate(inorder)}
        pre_idx = 0

        def build(lo, hi):  # inorder range [lo, hi]
            nonlocal pre_idx
            if lo > hi:
                return None
            root_val = preorder[pre_idx]
            pre_idx += 1
            root = TreeNode(root_val)
            mid = pos[root_val]
            root.left = build(lo, mid - 1)
            root.right = build(mid + 1, hi)
            return root

        return build(0, len(inorder) - 1)