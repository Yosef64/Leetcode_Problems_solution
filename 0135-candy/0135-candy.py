class Solution:
    def candy(self, ratings: List[int]) -> int:
        can ,csum = [1]*len(ratings), 0
        for inx in range(1,len(ratings)):
            if ratings[inx]>ratings[inx-1]:
                can[inx] = can[inx - 1] + 1

        for inx in range(len(ratings) - 2,-1,-1):
            if ratings[inx]>ratings[inx+1]:
                can[inx] = max(can[inx],can[inx+1] + 1)
                csum += can[inx]
        # print(can)
        return sum(can)

        