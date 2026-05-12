class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        c=Counter(nums)
        check=[]
        for i,j in c.items():
            check.append([j,i])
        check.sort()
        res=[]
        while len(res)<k:
            res.append(check.pop()[1])
        return res

        
        
        
