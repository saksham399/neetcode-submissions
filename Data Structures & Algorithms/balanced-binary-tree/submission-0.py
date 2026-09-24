# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root:
            if abs(self.maxHeight(root.left)-self.maxHeight(root.right)) <= 1:
                return self.isBalanced(root.left) and self.isBalanced(root.right)
            else:
                return False
        return True

    def maxHeight(self, root: Optional[TreeNode]) -> int:
        if root:
            return 1 + max(self.maxHeight(root.left),self.maxHeight(root.right))
        return 0
        