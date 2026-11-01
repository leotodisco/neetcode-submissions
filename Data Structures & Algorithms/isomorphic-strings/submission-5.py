class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hmS = dict()
        for i in range(len(s)):
            if s[i] in hmS:
                if hmS[s[i]] != t[i]:
                    return False

            hmS[s[i]] = t[i]

        for k, v in hmS.items():
            for k1, v1 in hmS.items():
                if v == v1 and k!=k1:
                    return False
        
        return True
            