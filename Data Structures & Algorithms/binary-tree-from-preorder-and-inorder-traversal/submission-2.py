# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        prequeue = deque(preorder)
        inorder_map = {val: i for i, val in enumerate(inorder)}
        def buildTreeHelper(inorder, l, r):
            if l >= r:
                return None
            rootval = prequeue.popleft()
            #print(rootval)
            index = inorder_map[rootval]
            rootnode = TreeNode(rootval)
            rootnode.left = buildTreeHelper(inorder, l, index)
            rootnode.right = buildTreeHelper(inorder, index+1, r)
            return rootnode
        return buildTreeHelper(inorder, 0, len(inorder))