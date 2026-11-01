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
            if c in hmS2:
                hmS2[c] = hmS2[c]+1
            else:
                hmS2[c] = 1
            
            if sum(hmS2.values()) == len(s1):
                flagIsEqual = True
                for k,v in hmS1.items():
                    if hmS2.get(k) != v:
                        flagIsEqual = False
                        continue
                
                for k,v in hmS2.items():
                    if hmS1.get(k) != v:
                        flagIsEqual = False
                        continue
                
                if flagIsEqual:
                    return True    
                        
                toRemoveChar = s2[index-len(s1)+1]
                hmS2[toRemoveChar] = hmS2[toRemoveChar]-1
                if hmS2[toRemoveChar] == 0:
                    hmS2.pop(toRemoveChar)
        
        return False
            

