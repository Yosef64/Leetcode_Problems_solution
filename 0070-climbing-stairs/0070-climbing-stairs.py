class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==0:
            return n
        ls=[0]*n
        ls[0],ls[1]=1,2
        for i in range(2,n):
            ls[i]=ls[i-1]+ls[i-2]
        return ls[-1]
        