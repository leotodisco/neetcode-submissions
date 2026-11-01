class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed)%3 != 0:
            f = [0] + flowerbed + [0]
        else:
            f = flowerbed

        for i in range(1, len(f) - 1):
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
                f[i] = 1
                n -= 1

        return n <= 0

