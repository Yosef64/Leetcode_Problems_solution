class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        qualityRatio = [[wage[ind]/quality[ind],quality[ind]] for ind in range(len(quality))]
        qualityRatio.sort()
        heap , kQuality = [] , 0
        ans = float("infinity")
        for ratio , quality in qualityRatio:
            heappush(heap,-quality)
            kQuality += quality
            if len(heap) > k:
                kQuality += heappop(heap)
            if len(heap) == k:
                ans = min(ans,kQuality * ratio)
        return ans




        
        