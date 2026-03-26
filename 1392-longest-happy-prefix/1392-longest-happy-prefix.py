class Solution:
    def longestPrefix(self, s: str) -> str:
     
        n = len(s)
        lps = [0] * n

        a = 0   # plays role of "length" (prefix pointer)
        b = 1   # current index

        while b < n:
            if s[a] == s[b]:
                a += 1
                lps[b] = a
                b += 1
            else:
                if a != 0:
                    a = lps[a - 1]
                else:
                    lps[b] = 0
                    b += 1

        return s[:lps[-1]]

        