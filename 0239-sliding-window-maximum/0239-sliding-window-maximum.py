class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

        dq = deque()
        res = []

        for i in range(len(nums)):
            # remove elements out of window
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # remove smaller elements (useless ones)
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # store result after first window
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res