# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = root.val
        self.cnt = k

        def visit(node):
            if not node:
                return

            visit(node.left)
            if self.cnt == 0:
                return 
            self.cnt -= 1
            if self.cnt == 0:
                self.res = node.val
                return

            visit(node.right)

        visit(root)
        return self.res