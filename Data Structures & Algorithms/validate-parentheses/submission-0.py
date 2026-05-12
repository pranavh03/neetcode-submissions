class Solution:
    def isValid(self, s: str) -> bool:
        dicti={']':'[','}':'{',')':'('}
        stack=[]
        for c in s:
            if c in dicti:
                if stack and stack[-1]==dicti[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return False if stack else True

        