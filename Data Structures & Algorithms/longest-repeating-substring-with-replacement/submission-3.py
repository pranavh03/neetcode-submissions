class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        count={}
        strlen=0
        res=0
        for right in range(len(s)):
            count[s[right]]=count.get(s[right],0)+1
            strlen=max(strlen,count[s[right]])
            while (right-left+1)-strlen>k:
                count[s[left]]-=1
                left+=1
            res=max(right-left+1,res)
        return res






        