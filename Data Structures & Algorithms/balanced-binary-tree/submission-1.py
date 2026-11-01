# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def computeHeight(self, root):
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        return 1 + max(self.computeHeight(root.left), self.computeHeight(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        hLeft = self.computeHeight(root.left)
        hRight = self.computeHeight(root.right)
        return (
            abs(hRight - hLeft) < 2 and
            self.isBalanced(root.left) and
            self.isBalanced(root.right)
        )


        

