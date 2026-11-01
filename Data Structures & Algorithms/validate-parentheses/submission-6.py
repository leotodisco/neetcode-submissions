class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")":"(",
        "}":"{",
        "]":"["
        }

        for c in s:
            if c in closeToOpen.values():
                stack.append(c)
            else:
                if not stack or closeToOpen[c] != stack.pop():
                    return False
        
        return not stack