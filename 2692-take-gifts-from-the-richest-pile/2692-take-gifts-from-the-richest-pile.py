class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        res = sum(gifts)
        heap = []
        for num in gifts:
            heappush(heap,-num)
        # print(heap)
        for _ in range(k):
            pile = -heappop(heap)
            # print(pile)
            sq = int(pile ** 0.5)
            res -= (pile-sq)
            heappush(heap,-sq)
        return res
        