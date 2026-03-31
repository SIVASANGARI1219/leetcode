class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort(); res = set()
        for i in range(len(nums)):
            if i and nums[i]==nums[i-1]: continue
            seen = set()
            for j in range(i+1, len(nums)):
                x = -nums[i]-nums[j]
                if x in seen: res.add((nums[i], x, nums[j]))
                seen.add(nums[j])
        return [list(t) for t in res]