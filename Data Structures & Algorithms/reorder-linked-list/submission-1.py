# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head != None or head.next != None:
            start, smid, emid = head, head, head
            while emid and emid.next:
                smid = smid.next
                emid = emid.next.next
            #print(smid.val)
            #print(start.val)
            prev, curr = None, smid.next
            smid.next = None  
            
            while curr:
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp
            '''
            0 1 2 3 4 5 6
            step 1
            start 0
            smid 3
            0 3 1 2 3 
            4 5 6
            step 2
            start 1
            smid 4
            0 3 1 4 2 3
            5 6
            step 3
            start 2
            smid 5
            0 3 1 4 2 5 3
            6
            step 4
            start 3 
            smid 6
            0 3 1 4 2 5 3 6 none
            '''
            while prev:
                #print("Here")
                temp1 = start.next
                temp2 = prev.next
                start.next = prev
                prev.next = temp1
                
                start = temp1
                prev = temp2
                #print(start.val)
                
        

