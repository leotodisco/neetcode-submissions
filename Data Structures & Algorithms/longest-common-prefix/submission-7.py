class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i >= len(s):
                    return res
                if i<len(s) and s[i] != strs[0][i]:
                    return res
            res += strs[0][i]

        return res
                