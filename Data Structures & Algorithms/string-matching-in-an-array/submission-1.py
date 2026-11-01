class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for index, w in enumerate(words):
            for i in range(0, len(words)):
                if i!=index and w in words[i]:
                    res.append(w)
                    break

        return res