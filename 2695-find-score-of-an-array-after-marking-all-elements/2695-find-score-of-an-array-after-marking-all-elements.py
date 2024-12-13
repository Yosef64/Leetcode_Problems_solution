class Solution:
    def findScore(self, nums: List[int]) -> int:
        heap ,marked = [], set()
        score = 0
        for inx,val in enumerate(nums):
            heappush(heap,[val,inx])
        while heap:
            val,inx = heappop(heap)

            if inx not in marked:
                
                score += val
            
                marked.add(inx)
                marked.add(inx-1)
                marked.add(inx+1)
        return score

