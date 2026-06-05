from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s or not t:
            return ""

        need = Counter(t)
        required = len(need)

        formed = 0
        window = {}

        left = 0
        ans = (float("inf"), 0, 0)

        for right in range(len(s)):

            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                formed += 1

            while left <= right and formed == required:

                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]