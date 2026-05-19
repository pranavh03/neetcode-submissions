class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        final=list(set(sorted(nums)))
        final.sort()
      

        count=[0]*len(nums)
        number=0
        if len(nums)==0: return 0
        for i in range(len(final)-1):
            if final[i]+1==final[i+1]:
                count[number]+=1
                
            else:
              
                number+=1
        return max(count)+1
        


        