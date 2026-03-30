class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = set()
        b = 0
        c = 0
        for r in range(len(s)):
            while s[r] in a:
                a.remove(s[b])
                b += 1
            a.add(s[r])
            c = max(c, r-b+1)
        return c