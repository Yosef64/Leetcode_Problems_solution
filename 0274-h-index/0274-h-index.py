class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n ,res = len(citations) , 0

        for ind in range(n-1,-1,-1):
            if citations[ind] < n - ind:return res

            res += 1
        return res