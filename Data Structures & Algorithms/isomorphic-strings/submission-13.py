class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapS = dict()
        mapT = dict()

        for index, char in enumerate(s):
            charT = t[index]

            if (char in mapS and mapS[char]!=charT) or (charT in mapT and mapT[charT]!=char):
                return False
            
            mapS[char] = charT
            mapT[charT] = char
        
        return True