class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n+1)]
        res = []

        def dfs(i, cur):
            if i >= len(nums):
            
                if len(cur) == k:
                    res.append(cur.copy())
                return

            
            cur.append(nums[i])
            dfs(i+1, cur)
            cur.pop()
            dfs(i+1, cur)

        dfs(0, [])
        return res
        