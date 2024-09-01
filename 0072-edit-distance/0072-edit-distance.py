class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo , n , m = {} , len(word1),len(word2)
        def dp(i,j):
            if i == n or j == m:
                return max(n-i,m-j)
            if (i,j) in memo:return memo[(i,j)]
            ignore = float("inf")
            if word1[i] == word2[j]:
                ignore = dp(i+1,j+1)
            ins = 1 + dp(i,j+1)
            delete = 1 + dp(i+1,j)
            rep = 1 + dp(i+1,j+1)
            memo[(i,j)] = min(ignore,ins,delete,rep)
            return memo[(i,j)]
        return dp(0,0)
        