class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        ans , dic = 1 , {}
        for ind in range(len(arr)-1,-1,-1):
            t = arr[ind] + difference 
            if t in dic:
                dic[arr[ind]] = 1+dic[t]
                
            else:
                dic[arr[ind]] = 1
            ans = max(ans,dic[arr[ind]])
        return ans


