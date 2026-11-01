class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        hmS1 = {}
        for c in s1:
            if c in hmS1:
                hmS1[c] = hmS1[c]+1
            else:
                hmS1[c] = 1
        
        hmS2 = {}
        for index, c in enumerate(s2):
            hmS2[c] = hmS2.get(c, 0) + 1
            
            if index >= len(s1):        
                toRemoveChar = s2[index-len(s1)]

                hmS2[toRemoveChar] = hmS2[toRemoveChar]-1
                if hmS2[toRemoveChar] == 0:
                    hmS2.pop(toRemoveChar)

            if hmS2 == hmS1:
                return True
        
        return False
            

