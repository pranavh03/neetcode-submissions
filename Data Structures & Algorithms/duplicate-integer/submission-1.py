class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num=[]
        for i in nums:
            if i not in num:
                num.append(i)
            elif i in num:
                return True
        return False
        