# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count =0
        def travel(root, val):
            nonlocal count
            if (root == None):
                return
            elif(root.left== None and root.right==None and root.val >= val):
                count = count +1
                return 
            else:
                if(val > root.val):
                    travel(root.left, val)
                    travel(root.right, val)
                else:
                    count = count +1
                    travel(root.left, root.val)
                    travel(root.right, root.val)
        if root == None:
            return 0
        travel(root, root.val)
        return count
        