class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n , m = len(nums1) , len(nums2)
        dp = [[0] * ( n + 1) for _ in range( m + 1)]
        ans = 0
        for col in range(1,n + 1):
            for row in range(1, m +1):
                if nums1[col - 1] == nums2[row -1]:
                    dp[row][col] = dp[row-1][col - 1] + 1
                    ans = max(ans,dp[row][col])
        return ans