class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openingPars = {'{', '[', "("}
        closingPars = {'}', ']', ")"}

        for char in s:
            if char in openingPars:
                stack.append(char)
            elif char in closingPars:
                if not stack:
                    return False
                top = stack.pop()
                if char == '}' and top != '{':
                    return False
                if char == ']' and top != '[':
                    return False
                if char == ')' and top != '(':
                    return False
            else:
                return False
        
        return not stack