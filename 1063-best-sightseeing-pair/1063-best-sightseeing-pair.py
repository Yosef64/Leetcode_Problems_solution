class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxSpot , d = values[-1] , len(values) - 1
        ans = 0
        for ind in range(len(values)- 2,-1,-1):
            ans = max(ans,maxSpot+values[ind]+(ind-d))
            if values[ind] >= maxSpot + (ind-d):
                maxSpot , d = values[ind] , ind
        return ans

        