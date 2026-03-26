class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
    
        for i in range(n-1, 0, -1):   # try largest first
            if s[:i] == s[n-i:]:
                return s[:i]
    
        return ""

        