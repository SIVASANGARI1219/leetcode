class Solution:
    def largestRectangleArea(self,h):
        stack, max_area = [], 0
        h.append(0)
        for i in range(len(h)):
            while stack and h[stack[-1]] > h[i]:
                height = h[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area