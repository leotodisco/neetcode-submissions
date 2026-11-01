# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = root.val
        cnt = k

        def visit(node):
            nonlocal res, cnt
            if not node:
                return

            visit(node.left)
            if cnt == 0:
                return 
            cnt -= 1
            if cnt == 0:
                res = node.val
                return

            visit(node.right)

        visit(root)
        return res