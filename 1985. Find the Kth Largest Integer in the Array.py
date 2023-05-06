class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        lst=[int(x) for x in nums]
        lst.sort()
        return str(lst[len(lst)-k])
        