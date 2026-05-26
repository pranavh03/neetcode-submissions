class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0
        left=0
        maxcout=0
        count={}

        for i in range(len(s)):
            count[s[i]]=1+count.get(s[i],0)
            maxcout=max(maxcout,count[s[i]])
            while (i-left+1)-maxcout>k:
                count[s[left]] -=1
                left+=1
            res=max(res,i-left+1)
        return res





        