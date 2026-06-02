class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = [ch.lower() for ch in s if ch.isalnum()]
        return chars == chars[::-1]