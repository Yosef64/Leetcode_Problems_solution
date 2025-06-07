class Solution:
    def clearStars(self, s: str) -> str:
        heap , dic= [],{inx:s[inx] for inx in range(len(s)) }
        heapify(heap)
        for indx in range(len(s)):
            if s[indx] == "*":
                char, inx = heappop(heap)
                dic[-inx] = None
                continue
            
            heappush(heap,[s[indx],-indx])
        ans = ""
        for inx in range(len(s)):
            if dic[inx] and dic[inx] != "*":
                ans += dic[inx]
        return ans


        