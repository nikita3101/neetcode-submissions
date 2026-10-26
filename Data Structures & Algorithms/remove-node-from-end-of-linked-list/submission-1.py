# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        prev = None
        if head and n == 1 and head.next == None:
            return None
        while n > 0 and fast:
            fast = fast.next
            n = n-1
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        if slow == head:
            head = head.next
        elif prev and slow:
            prev.next = slow.next
        return head


        