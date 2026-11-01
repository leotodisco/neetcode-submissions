class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] <= target and row[-1] >= target:
                if self.search(row, target):
                    return True

        return False

    def search(self, row, target) -> bool:
        l = 0
        r = len(row)-1
        while l<=r:
            mid = (l+r)//2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                r = mid-1
            else:
                l = mid+1
        return False