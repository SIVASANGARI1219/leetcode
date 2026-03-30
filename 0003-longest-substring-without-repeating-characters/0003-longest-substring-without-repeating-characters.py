class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        for i in range(len(s)):
            seen = []   # to store characters in current substring

            for j in range(i, len(s)):
                if s[j] in seen:
                    break
                seen.append(s[j])
            
            max_len = max(max_len, len(seen))

        return max_len