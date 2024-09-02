class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dp(word,m,op):
            nonlocal ans
            if m == n:
                ans.append(word+')'*op)
                return 
            if op == 0:
                return dp(word+'(',m+1,1)
            return dp(word+'(',m+1,op+1) or dp(word+')',m,op - 1)
        dp('(',1,1)
        return ans
        