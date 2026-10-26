# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(head)-> Optional[ListNode]:
            prev = None
            while head:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            return prev

        if head == None:
            return True
        if head and head.next == None:
            return True
        else:
            slow = head
            fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            if fast:
                slow = slow.next
            print(slow.val)
            slow = reverse(slow)
            print(slow.val)
            while slow:
                if head.val != slow.val:
                    return False
                head = head.next
                slow= slow.next
            if slow == None:
                return True
