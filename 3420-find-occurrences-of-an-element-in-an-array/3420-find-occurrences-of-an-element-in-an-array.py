class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        dic ,count = {}, 0
        for inx,val in enumerate(nums):
            if val == x:
                count += 1
                dic[count] = inx
        ans = []
        for occ in queries:
            ans.append(dic[occ] if occ in dic else -1)
        return ans
        