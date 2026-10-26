# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxdiameter = 0
        def diameterHelper (root) -> int:
            nonlocal maxdiameter
            if root is None:
                return 0
            else:
                left = diameterHelper(root.left)
                right = diameterHelper(root.right)
                if(maxdiameter < (left +right)):
                    maxdiameter = left +right
                return max (left, right) + 1
        diameterHelper(root)
        return maxdiameter


      