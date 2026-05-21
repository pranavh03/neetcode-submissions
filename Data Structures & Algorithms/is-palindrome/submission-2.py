class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=''
        for i in range(len(s)):
            if  s[i].isalnum() and s[i]!=' ':
                string+=s[i]
                        
        for i,j in zip(range(0,len(string)),range(-1,-len(string),-1)):
            if i==j :
                True
            if string[i].upper()!=string[j].upper():
                return False
        return True
            
