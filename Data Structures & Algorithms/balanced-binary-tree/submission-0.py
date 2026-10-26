# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root:Optional[TreeNode]):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            else:
                return max(height(root.left), height(root.right))+1

        if not root:
            return True
        if not root.left and not root.right:
            return True
        else:
            lheight=height(root.left)
            rheight=height(root.right)
            if(abs(lheight-rheight)>1):
                return False
            return self.isBalanced(root.left) and self.isBalanced(root.right)
