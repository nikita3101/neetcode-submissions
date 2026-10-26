# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def pathSum(root, curSum) -> bool:
            if root == None:
                return False
            if root.left== None and root.right == None:
                return curSum+root.val == targetSum
            else:
                left = pathSum(root.left, curSum+root.val)
                right = pathSum(root.right, curSum+root.val)
                return left or right
        
        return pathSum(root, 0)