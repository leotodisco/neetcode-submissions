class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hms = {}
        for ch in s:
            hms[ch] = hms.get(ch,0)+1

        hmt = {}
        for ch in t:
            hmt[ch] = hmt.get(ch,0)+1

        if hms.keys() != hmt.keys():
            return False
        
        for k, v in hms.items():
            if hmt[k] != v:
                return False

        return True        