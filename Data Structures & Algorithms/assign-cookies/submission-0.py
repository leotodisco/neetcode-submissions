class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gPointer = 0
        sPointer = 0

        while gPointer < len(g):
            while sPointer < len(s) and g[gPointer] > s[sPointer]:
                sPointer+=1
            if sPointer == len(s):
                break
            
            gPointer+=1
            sPointer+=1

        return gPointer

