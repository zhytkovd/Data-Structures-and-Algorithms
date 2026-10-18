from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {")":"(", "]":"[", "}":"{"}
        stack = deque()

        for c in s:
            if c in close_to_open:
                # if empty and last element doesn't equal closing paranth.
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        if stack:
            return False
        else:
            return True
            


            
            
            