class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dic={')':'(',']':'[','}':'{'}
        for i in s:
            if i in dic:
                if not stack or stack.pop() != dic[i]:
                    return False
            else:
                stack.append(i)
        return True if len(stack)==0 else False
        