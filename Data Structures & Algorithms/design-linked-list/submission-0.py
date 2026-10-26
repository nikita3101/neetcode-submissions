class ListNode:
    def __init__(self, val:int):
        self.val = val
        self.next= None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        cur = self.head
        while index >0 and cur:
            cur = cur.next
            index = index - 1
        if(cur):
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        cur = ListNode(val)
        cur.next = self.head
        self.head = cur
        print("Head")
        while cur:
            print(cur.val, end=", ")
            cur = cur.next

    def addAtTail(self, val: int) -> None:
        cur = self.head 
        while cur and cur.next:
            cur = cur.next
        if (cur and cur.next == None):
            cur.next = ListNode(val)
        
        print("Tail")
        
        while cur:
            print(cur.val, end=", ")
            cur = cur.next

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.head
        prev = None
        while index >0 and cur:
            index = index - 1
            prev = cur
            cur = cur.next
        if prev:
            n = prev.next 
            temp = ListNode(val)
            prev.next = temp
            temp.next = n
        print("atIndex")
        cur = self.head
        while cur:
            print(cur.val, end=", ")
            cur = cur.next

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head
        prev = None
        while index >0 and cur:
            index = index - 1
            prev = cur
            cur = cur.next
        if prev and prev.next:
            prev.next = prev.next.next
        cur = self.head
        print("Delete")
        while cur:
            print(cur.val, end=", ")
            cur = cur.next



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)