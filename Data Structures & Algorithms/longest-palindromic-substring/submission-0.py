class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]  # the valid palindrome substring

        res = ""
        for i in range(len(s)):
            # Odd-length palindrome (centered at i)
            p1 = expand_from_center(i, i)
            # Even-length palindrome (centered between i and i+1)
            p2 = expand_from_center(i, i + 1)

            # Choose the longer palindrome
            if len(p1) > len(res):
                res = p1
            if len(p2) > len(res):
                res = p2

        return res
