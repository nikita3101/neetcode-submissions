# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = [0]
        def kthSmallestRecu(root: Optional[TreeNode], k: int, count: int):
            if(root == None):
                return -1
            else:
                val = kthSmallestRecu(root.left, k, cnt)
                if (val != -1):
                    return val
                cnt[0] += 1
                if(cnt[0] == k):
                    return root.val
                right = kthSmallestRecu(root.right, k, cnt)
                return right
        return kthSmallestRecu(root, k, cnt)
        