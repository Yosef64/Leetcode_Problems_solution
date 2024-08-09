class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        if n == 2:
            return 1
        ls = [0]*n
        ls[0], ls[1], ls[2] = 1 , 1 , 2
        for i in range(3,n):
            ls[i] = ls[i-1]+ls[i-2]+ls[i-3]
        return ls[-1]
        
        