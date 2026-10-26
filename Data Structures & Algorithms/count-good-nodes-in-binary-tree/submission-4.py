# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        def goodNodeHelp (root, val) -> int:
            if root == None:
                return 0
            else:
                if(root.val >= val):
                    return goodNodeHelp(root.left, root.val) + goodNodeHelp(root.right, root.val) + 1
                else:
                    return goodNodeHelp(root.left, val) + goodNodeHelp(root.right, val) 
        return goodNodeHelp(root, root.val)