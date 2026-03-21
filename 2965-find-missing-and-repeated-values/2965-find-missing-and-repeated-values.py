class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        nums = sum(grid, [])
        for i in range(1, len(nums)+1):
            if nums.count(i) == 2: a = i
            if nums.count(i) == 0: b = i
        return [a, b]