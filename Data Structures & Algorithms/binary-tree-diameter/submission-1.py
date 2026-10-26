# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        l=0
        def dHelper(root: Optional[TreeNode]):
            nonlocal l
            if(root==None):
                return 0
            else:
                lpath=dHelper(root.left)
                rpath=dHelper(root.right)
                l=max(l, lpath+rpath)
                return max(lpath,rpath)+1
        
        dHelper(root)
        return l
