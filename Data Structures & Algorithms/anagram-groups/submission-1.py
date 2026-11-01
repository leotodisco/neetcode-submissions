from collections import defaultdict

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)

        for i in range(len(strs)):
            arr = [0]*26
            for ch in strs[i]:
                index = ord(ch)-ord('a')
                arr[index] += 1
            
            count[tuple(arr)].append(strs[i])
        
        return list(count.values())