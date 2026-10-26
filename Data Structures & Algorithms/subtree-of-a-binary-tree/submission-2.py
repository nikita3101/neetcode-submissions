# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(root, subRoot) -> bool:
            if root == None and subRoot == None:
                return True
            if((root != None and subRoot == None) or (root == None and subRoot != None)):
                return False
            else:
                if(root.val != subRoot.val):
                    return False
                else:
                    return isSame(root.left,subRoot.left) and isSame(root.right, subRoot.right)


        if root == None and subRoot == None:
            return True
        if (root == None and subRoot !=None) or (root != None and subRoot ==None):
            return False
        else:
            if(root.val == subRoot.val and isSame(root, subRoot)):
                return True
            else:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)