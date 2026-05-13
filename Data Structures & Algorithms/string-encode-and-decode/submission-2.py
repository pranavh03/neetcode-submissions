class Solution:

    def encode(self, strs: List[str]) -> str:
        str1=''
        for i in strs:
            str1+=i
            str1+='NAN'
        return str1

    def decode(self, s: str) -> List[str]:
       result=s.split('NAN')
       return result[0:len(result)-1]