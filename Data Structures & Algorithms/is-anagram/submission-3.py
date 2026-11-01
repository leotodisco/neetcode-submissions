class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmS = dict()
        hmT = dict()
        for char in s:
            hmS[char] = hmS.get(char, 0) + 1

        for char in t:
            hmT[char] = hmT.get(char, 0) + 1

        if not hmS.keys() == hmT.keys():
            return False

        for char, nOccs in hmS.items():
            if not nOccs == hmT.get(char):
                return False
        
        return True
