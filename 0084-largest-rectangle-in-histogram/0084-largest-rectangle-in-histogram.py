class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
       
        n, max_area = len(heights), 0
        for i in range(n):
            h, l, r = heights[i], i, i
            while l > 0 and heights[l-1] >= h: l -= 1
            while r < n-1 and heights[r+1] >= h: r += 1
            max_area = max(max_area, h * (r - l + 1))
        return max_area