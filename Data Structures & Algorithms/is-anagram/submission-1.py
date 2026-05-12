class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=list(s)
        t=list(t)
        s.sort()
        t.sort()
        if ''.join(s)==''.join(t):
            return True
        else:
            return False