class Solution:
    def maxScore(self, s: str) -> int:
        total= sum (int(num) for num in s)
        left , ans = 0, 0
        for i in range(len(s)-1):
            total -= int(s[i])
            if s[i] == '0':
                left += 1
            ans = max(ans,total + left)
        return ans

        