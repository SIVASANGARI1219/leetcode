class Solution:
    def longestPrefix(self, s: str) -> str:
        lps = [0] * len(s)
        a = 0

        for b in range(1, len(s)):
            while a > 0 and s[a] != s[b]:
                a = lps[a - 1]
            if s[a] == s[b]:
                a += 1
            lps[b] = a
 
        return s[:lps[-1]]    
       

        