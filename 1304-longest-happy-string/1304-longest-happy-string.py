class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap , ans =  [[-a,"a"],[-b,"b"],[-c,"c"]] , ""
        heapify(heap)
        while True:
            n , char = heappop(heap)
            if n == 0:return ans
            if len(ans) >= 2 and ans[-2:] == char * 2:
                if heap[0][0] == 0:return ans
                n2 , char1 = heappop(heap)
                ans += char1
                heappush(heap,[n2+1,char1])
                heappush(heap,[n,char])
            else:
                ans += char
                heappush(heap,[n+1,char])

