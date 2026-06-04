class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter={}
        for i in range(len(nums)):
            counter[nums[i]]=counter.get(nums[i],0)+1
        new=sorted([[j,i] for i,j in counter.items()],reverse=True)
        final=[]
    
        for i,item in zip(range(k),new):
            final.append(item[1])
        return final








        