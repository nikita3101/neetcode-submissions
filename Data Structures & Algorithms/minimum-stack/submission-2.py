class MinStack:

    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()

    def push(self, val: int) -> None:
        self.stack1.append(val)
        if(len(self.stack2) == 0 or (len(self.stack2) != 0 and self.stack2[-1] >= val)):
            self.stack2.append(val)

    def pop(self) -> None:
        val=self.stack1.pop()
        if(len(self.stack2) != 0 and self.stack2[-1] == val):
            self.stack2.pop()

    def top(self) -> int:
        if(len(self.stack1) != 0 ):
            return self.stack1[-1]
        return -1

    def getMin(self) -> int:
        if(len(self.stack2) != 0 ):
            return self.stack2[-1]
        return -1
        
