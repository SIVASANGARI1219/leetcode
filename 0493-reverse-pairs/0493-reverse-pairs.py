class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(arr):
            if len(arr) <= 1: return arr, 0
            
            mid = len(arr)//2
            left, c1 = merge_sort(arr[:mid])
            right, c2 = merge_sort(arr[mid:])
            
            count = c1 + c2
            j = 0
            for x in left:
                while j < len(right) and x > 2 * right[j]:
                    j += 1
                count += j
            
            return sorted(left + right), count
        
        return merge_sort(nums)[1]
        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] > 2 * nums[j]: count += 1
        # return count        