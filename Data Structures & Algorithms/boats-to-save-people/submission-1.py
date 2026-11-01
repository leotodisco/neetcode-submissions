class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        l=0
        r = len(people)-1
# 1,2,4,5 limit=6
# 
        while l<=r:
            remain = limit - people[r]
            r-=1 # punto sempre alla persona più pesante rimasta
            res+=1
            if l <= r and remain >= people[l]: # se ci va anche la + leggera prendi anche la leggera
                l += 1
        return res


