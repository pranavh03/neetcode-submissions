class Solution:
    def findMin(self, nums: List[int]) -> int:

        left=0
        right=len(nums)-1
        if nums[0]<nums[-1] or len(nums)==1:
            return nums[0]

        while left<=right:

            m=(left+right)//2
            if nums[m]>nums[m+1]:
                return nums[m+1]
            
            elif nums[m]<nums[m-1]:
                return nums[m]
            else:
                if nums[m]>nums[right]:
                    left=m+1
                else:
                    right=m-1
        

