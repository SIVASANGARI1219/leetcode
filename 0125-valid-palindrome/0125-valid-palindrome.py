class Solution(object):
    def isPalindrome(self, s):
        cleaned = ""

    # Step 1: Remove non-alphanumeric and convert to lowercase
        for ch in s:
            if ch.isalnum():      # keeps only letters and numbers
                cleaned += ch.lower()

    # Step 2: Check palindrome
        return cleaned == cleaned[::-1]