class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap , ans = [] , ""
        for ls in [[-a,"a"],[-b,"b"],[-c,"c"]]:
            heapq.heappush(heap,ls)
        
        while True:
            n , char = heappop(heap)
            if n == 0:return ans
            if len(ans) >= 2 and ans[-2:] == char * 2:
                n2 , char1 = heappop(heap)
                
                if n2 == 0:return ans

                ans += char1
                heappush(heap,[n2+1,char1])
                heappush(heap,[n,char])
            else:
                ans += char
                heappush(heap,[n+1,char])

