from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hm = defaultdict(set)

        for index, c in enumerate(s):
            hm[c].add(t[index])
        
        for k, v in hm.items():
            if len(v) != 1:
                return False
        
        x = []
        for v in hm.values():
            x.extend(v)
        if len(x) != len(set(x)):
            return False
        return True
