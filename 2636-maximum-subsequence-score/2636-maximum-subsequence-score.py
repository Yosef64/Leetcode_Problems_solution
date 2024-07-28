import heapq
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        lst=[[nums2[ind],nums1[ind]] for ind in range(len(nums1))]
        lst.sort(key=lambda x:(-x[0],-x[1]))
        heap = []
        i , sm = 0 , 0
        ef , prd = float("infinity") , float("-infinity")
        while i < k:
           
            heapq.heappush(heap,lst[i][1])
            ef=min(ef,lst[i][0])
            sm+=lst[i][1]
            i+=1
        prd=max(prd,sm*ef)
        while i < len(nums1):
            x=heapq.heappop(heap)
            sm-=x
            # y=lst.pop(0)
            heapq.heappush(heap,lst[i][1])
            ef = lst[i][0]
            sm+=lst[i][1]
            prd=max(prd,sm*ef)
            i += 1
        return prd