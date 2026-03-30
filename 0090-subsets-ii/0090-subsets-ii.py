class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]; start = 0
        for i in range(len(nums)):
            start = 0 if i == 0 or nums[i] != nums[i-1] else prev
            prev = len(res); res += [r + [nums[i]] for r in res     [start:prev]]
        return res