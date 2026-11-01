class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        hm = {}

        for a, b in trust:
            if a not in hm:
                hm[a] = {"uscenti": [], "entranti": []}

            if b not in hm:
                hm[b] = {"uscenti": [], "entranti": []}


            entranti_lst = hm.get(b, {}).get("entranti", [])
            entranti_lst.append(a)
            hm[b]["entranti"] = entranti_lst

            uscenti_lst = hm.get(a, {}).get("uscenti", [])
            uscenti_lst.append(b)
            hm[a]["uscenti"] = uscenti_lst


        for a, b in trust:
            if not hm[a]["uscenti"] and len(hm[a]["entranti"]) == n-1:
                return a

            if not hm[b]["uscenti"] and len(hm[b]["entranti"]) == n-1:
                return b
        
        return -1