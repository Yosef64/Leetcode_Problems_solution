class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        ans = [float("-inf"),float("inf")]
        minHeap ,maxHeap = [] ,[]
        maxEle = float("-inf")
        for ind in range(len(nums)):
            maxEle = max(maxEle,nums[ind][0])
            # print(nums[ind][0])
            heapq.heappush(minHeap,[nums[ind][0],0,ind])
            
        while True:
            minVal , minInd,Ind = heapq.heappop(minHeap)
            if maxEle - minVal < ans[1] - ans[0]:
                ans = [minVal , maxEle]
            if minInd + 1 == len(nums[Ind]):
                return ans
            heapq.heappush(minHeap,[nums[Ind][minInd+1],minInd+1,Ind])
            maxEle = max(maxEle,nums[Ind][minInd + 1])
            
            


 
