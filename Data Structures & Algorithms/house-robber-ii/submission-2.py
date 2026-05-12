class Solution:
    def rob(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return nums[0]
        
        def Robbing(nums):
            Rob1,Rob2=0,0
            for i in nums:
                temp=max(Rob1+i,Rob2)
                Rob1=Rob2
                Rob2=temp
            return Rob2
        return max(Robbing(nums[:-1]),Robbing(nums[1:]))




        