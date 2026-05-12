class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1
        leng=[]
        length=0
        i=0 
        j=1 #[2,3,4,4,5,10,20]
        while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                i+=1
                continue
            elif nums[i]+1==nums[i+1]:
                i+=1
                length+=1
            elif nums[i]+1!=nums[i+1]:
                i+=1
                length+=1
                leng.append(length)
                length=0 #[0,1,1,2,3,4,5,6]
        leng.append(length+1)
        return max(leng)