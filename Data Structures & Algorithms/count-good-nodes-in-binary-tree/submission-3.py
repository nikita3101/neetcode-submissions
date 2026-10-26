# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def goodHelper(root:TreeNode, val:int) -> int:
            if not root:
                return 0
            else:
                if(root.val>=val):
                    return 1 + goodHelper(root.left,root.val) +goodHelper(root.right,root.val)
                else:
                    return goodHelper(root.left,val) +goodHelper(root.right,val)

        
        if not root:
            return 0
        return goodHelper(root,root.val)