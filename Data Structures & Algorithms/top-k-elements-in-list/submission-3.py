class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in nums:
            count[i]=1+count.get(i,0)
        arr=[]
        for key,value in count.items():
            arr.append([value,key])
        arr.sort()
        result=[]
        for f in range(k):
            result.append(arr.pop()[1])
        return result



        