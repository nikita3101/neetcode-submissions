# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if(root == None):
            return True
        def validation(root, minval, maxval):
            if(root!=None):
                if(minval< root.val< maxval):
                    return validation(root.left, minval, root.val) and validation(root.right, root.val, maxval)
                else:
                    return False
            return True
        return validation(root, -1000000000, 1000000000)
            