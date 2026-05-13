class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[1]*len(nums)
        for i in range(len(nums)):
            res=1
            j=0
            for j in range(len(nums)) :
                if j==i:
                    continue
                res*=nums[j]
                
                
            result[i]=res
        return result
        