class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowLen = len(s1)
        hm1 = {}
        for c in s1:
            hm1[c] = hm1.get(c, 0)+1
        
        hm2 = {}
        l = 0
        for r in range(len(s2)):
            hm2[s2[r]] = hm2.get(s2[r], 0) + 1

            # se la finestra è diventata troppo grande elimino l e avanzo l di 1
            if r - l + 1 > windowLen:
                hm2[s2[l]] -= 1
                if hm2[s2[l]] == 0:
                    del hm2[s2[l]]
                l += 1

            if hm1 == hm2:
                return True
            
        return False