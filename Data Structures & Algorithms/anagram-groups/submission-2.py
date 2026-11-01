class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)

        for s in strs:
            s = s.lower()
            charArray = [0] * 26
            for c in s:
                pos = ord(c)-ord('a')
                charArray[pos] = charArray[pos]+1
            l = hm.get(tuple(charArray), [])
            l.append(s)
            hm[tuple(charArray)] = l
        return [l for l in hm.values()]
        