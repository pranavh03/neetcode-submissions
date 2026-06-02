class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=''
        for i in range(len(s)):
            if  s[i].isalnum() and s[i]!=' ':
                string+=s[i]
                     
        return string.lower()==string[::-1].lower()
            
