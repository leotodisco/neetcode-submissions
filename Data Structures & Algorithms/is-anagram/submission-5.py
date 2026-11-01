class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmS = dict()
        hmT = dict()

        for char in s:
            count = hmS.get(char, 0)
            hmS[char] = count+1
        
        for char in t:
            count = hmT.get(char, 0)
            hmT[char] = count+1
        
        if hmS.keys() != hmT.keys():
            return False
        
        for char, nOccurs in hmS.items():
            if hmT.get(char, 0) != nOccurs:
                return False

        return True