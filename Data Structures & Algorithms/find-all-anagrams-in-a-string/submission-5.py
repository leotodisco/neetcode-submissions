class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        hmP = {}
        for c in p:
            hmP[c] = hmP.get(c, 0) + 1
        
        res = []
        hmS = {}
        for index, c in enumerate(s):
            hmS[c] = hmS.get(c, 0)+1
            if index >= len(p):
                toRemoveChar = s[index-len(p)]
                hmS[toRemoveChar] -= 1
                if hmS[toRemoveChar] == 0:
                    hmS.pop(toRemoveChar)

            if hmS == hmP:
                res.append(index-len(p)+1)

        return res
