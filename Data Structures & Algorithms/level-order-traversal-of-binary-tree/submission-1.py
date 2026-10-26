# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        queue=deque()
        if not root:
            return []
        else:
            queue.append(root)
            queue.append('#')
            item=queue.popleft()
            while len(queue)>0 and item!='#':
                li=[]
                while item != '#':
                    #print(item.val)
                    li.append(item.val)
                    if item.left:
                        queue.append(item.left)
                    if item.right:
                        queue.append(item.right)
                    item=queue.popleft()
                    #print(item)
                res.append(li)
                #print(res)
                queue.append('#')
                item=queue.popleft()
            return res
                    


        
        