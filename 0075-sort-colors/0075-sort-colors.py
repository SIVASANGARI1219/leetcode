class Solution:
    def sortColors(self, nums: List[int]) -> None:
        c0, c1, c2 = nums.count(0), nums.count(1), nums.count(2)
        nums[:c0] = [0]*c0
        nums[c0:c0+c1] = [1]*c1
        nums[c0+c1:] = [2]*c2
  