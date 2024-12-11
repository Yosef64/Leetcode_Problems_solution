class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        arr = Counter(words)
        heap ,res= [],[]
        for key in arr:
            heappush(heap,[-arr[key],key])
        
        for _ in range(k):
            count,ele = heappop(heap)

            res.append(ele)
        return res
        