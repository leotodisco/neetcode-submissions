# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def fun(root, lst):
            if not root:
                return
            
            fun(root.left, lst)
            lst.append(root.val)
            fun(root.right, lst)
        l = []
        fun(root, l)
        return l

        