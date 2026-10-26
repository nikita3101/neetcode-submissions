class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for i in s:
            if(i == '{' or i == '[' or i == '('):
                stack.append(i)
            else:
                if(len(stack) == 0):
                    return False
                else:
                    if((i == '}' and stack[-1] == '{') or (i == ']' and stack[-1] == '[') or (i == ')' and stack[-1] == '(')  ) :
                        stack.pop()
                    else:
                        return False
        if len(stack) == 0:
            return True
        else:
            return False
        