class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left , windowSum = 0 , sum(arr[:k])
        ans = 0
        for right in range(k,len(arr)):
            if windowSum / k >= threshold:
                ans += 1
            windowSum += arr[right] - arr[left]
            left += 1
        if windowSum / k >= threshold:
            ans += 1
        return ans
        