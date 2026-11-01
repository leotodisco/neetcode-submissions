class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        area = 0

        while l<r:
            min_height = min(heights[l], heights[r])
            tmp_area = (r-l)*min_height
            area = max(area, tmp_area)

            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1



        return area