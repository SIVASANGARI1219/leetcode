class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def f(a):
            if len(a)<=1: return a,0
            l,c1=f(a[:len(a)//2]); r,c2=f(a[len(a)//2:])
            j=c=0
            for x in l:
                while j<len(r) and x>2*r[j]: j+=1
                c+=j
            return sorted(l+r), c+c1+c2
        return f(nums)[1]
        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] > 2 * nums[j]: count += 1
        # return count        