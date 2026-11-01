class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for s in strs:
            alphabet = [0]*26
            for char in s:
                alphabet_index = ord('a')-ord(char)
                alphabet[alphabet_index]+=1

            if tuple(alphabet) not in hm:
                hm[tuple(alphabet)] = []

            hm[tuple(alphabet)].append(s)
        
        return list(hm.values())
        
            

