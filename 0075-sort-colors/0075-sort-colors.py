class Solution:
    def sortColors(self, nums: List[int]) -> None:

        # counting the occurances like 2 is occuring 2 times...
        c0, c1, c2 = nums.count(0), nums.count(1), nums.count(2)
        
        # comparing and swaping elemets
        #    values*n 
        nums[:c0] = [0]*c0                
        nums[c0:c0+c1] = [1]*c1
        nums[c0+c1:] = [2]*c2





c0 = 2   # two 0s
c1 = 2   # two 1s
c2 = 2   # two 2s
  