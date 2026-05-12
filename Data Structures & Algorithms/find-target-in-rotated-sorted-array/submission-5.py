class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        n=len(nums)-1
        while l<r:
            m=(r+l)//2
            if nums[m]<nums[r]:
                r=m
            else:
                l=m+1
        midindex=l
        if  midindex==0:
            l,r=0,n
        elif target>=nums[0] and target<=nums[midindex-1]:
            l=0
            r=midindex-1

        else:
            l=midindex
            r=n

        while l<=r:
            m=(l+r)//2
            if nums[m]==target:
                return m
            elif nums[m]<target:
                l=m+1
            else:
                r=m-1
        return -1