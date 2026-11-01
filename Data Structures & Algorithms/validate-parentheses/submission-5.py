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
                if not stack:
                    return False
                top = stack.pop()
                if closeToOpen[c] != top:
                    return False
        
        return not stack