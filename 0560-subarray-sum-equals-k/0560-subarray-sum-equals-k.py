class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, s, d = 0, 0, {0:1}
        for num in nums:
            s += num
            if s - k in d: count += d[s - k]
            d[s] = d.get(s, 0) + 1
        return count