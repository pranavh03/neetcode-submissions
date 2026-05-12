class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums=numbers
        l,r=0,len(nums)-1
        while l<r:
            sums=nums[l]+nums[r]
            if target==sums:
                return [l+1,r+1]
                while l<r and nums[l]==nums[l+1]:
                    l+=1
                while l<r and nums[r]==nums[r-1]:
                    r-=1
            elif sums<target:
                l+=1
            else:
                r-=1

        