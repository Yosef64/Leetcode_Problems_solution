from sortedcontainers import SortedList
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        res = []
        window = SortedList(nums[:k])

        for i in range(k, len(nums)):
            if k % 2 == 1:
                median = window[k // 2]
            else:
                median = (window[k // 2] + window[k // 2 - 1]) / 2

            res.append(float(median))

            window.discard(nums[i - k])
            window.add(nums[i])

        # Process the last window
        if k % 2 == 1:
            median = window[k // 2]
        else:
            median = (window[k // 2] + window[k // 2 - 1]) / 2

        res.append(float(median))

        return res
            
        
        