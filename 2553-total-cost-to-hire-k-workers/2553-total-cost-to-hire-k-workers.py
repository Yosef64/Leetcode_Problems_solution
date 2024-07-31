class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        ans , left , right = 0 , 0 , n - 1
        heap1, heap2 = [] , []
        
        for _ in range(k):
            while len(heap1) < candidates and left <= right:
                heappush(heap1,costs[left])
                left += 1
            while len(heap2) < candidates and left <= right:
                heappush(heap2,costs[right])
                right -= 1
            
            if not heap1 or not heap2:
                if not heap1 and not heap2:break

                ans = ans + heappop(heap1) if heap1 else ans + heappop(heap2)
            else:
                if heap1[0] <= heap2[0]:
                    ans+= heappop(heap1)
                    continue
                ans += heappop(heap2)
        return ans


        
        
