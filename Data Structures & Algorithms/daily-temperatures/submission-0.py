class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        current=0
        result=[]
        while current<len(temperatures):
            for i in range(current+1,len(temperatures)):
                if temperatures[i]>temperatures[current]:
                    result.append(i-current)
                    current+=1
                    break
            else:
                result.append(0)
                current+=1
        return result

        