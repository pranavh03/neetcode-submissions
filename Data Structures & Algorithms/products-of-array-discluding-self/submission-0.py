class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r_mul=1
        l_mul=1
        n=len(nums)
        l_arr=[0]*n
        r_arr=[0]*n
        
        for i in range(n):
            j=-i-1
            r_arr[j]=r_mul
            l_arr[i]=l_mul
            l_mul *=nums[i]
            r_mul *=nums[j]
        return [l*r for l,r in zip(l_arr,r_arr)]

        