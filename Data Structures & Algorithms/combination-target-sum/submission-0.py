class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res,sol=[],[]
        def backtracking(i,curr_sum):
            if curr_sum==target:
                res.append(sol[:])
                return
            if curr_sum>target or i==len(nums):
                return
            backtracking(i+1,curr_sum)
            sol.append(nums[i])
            backtracking(i,curr_sum+nums[i])
            sol.pop()
        backtracking(0,0)
        return res




        