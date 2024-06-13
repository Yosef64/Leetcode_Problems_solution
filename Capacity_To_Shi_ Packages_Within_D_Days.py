class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        Max, Total = max(weights), sum(weights)

        l, h = Max, Total
        while l < h:
            mid = (l + h) // 2
            
            days_needed, curr_w = 1, 0
            for w in weights:
                if curr_w + w > mid:
                    days_needed += 1
                    curr_w = 0
                curr_w += w
            
            if days_needed > days:
                l = mid + 1
            else: 
                h = mid

        return l
