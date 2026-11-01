class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashMap = dict()
        for index, char in enumerate(s):
            if char in hashMap.keys() and hashMap[char] != t[index]:
                return False

            hashMap[char] = t[index]

        hashMapT = dict()
        for index, char in enumerate(t):
            if char in hashMapT.keys() and hashMapT[char] != s[index]:
                return False

            hashMapT[char] = s[index]
        
        for k, v in hashMap.items():
            if hashMapT[v] != k:
                return False
        
        return True