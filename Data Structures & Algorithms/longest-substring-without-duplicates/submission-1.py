class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Charset=set()
        l=0
        res=0
        for i in range(len(s)):
            while s[i] in Charset:
                Charset.remove(s[l])
                l+=1
            Charset.add(s[i])
            res=max(res,i-l+1)
        return res
