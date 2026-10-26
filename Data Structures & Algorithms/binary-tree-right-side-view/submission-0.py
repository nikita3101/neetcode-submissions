# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        if not root:
            return []
        else:
            q=deque()
            q.append(root)
            q.append('#')
            val=q.popleft()
            while len(q)>0 and val!='#' :
                res.append(val.val)
                while(val!='#'):
                    if(val.right):
                        q.append(val.right)
                    if(val.left):
                        q.append(val.left)
                    val=q.popleft()
                q.append('#')
                val=q.popleft()
            return res

