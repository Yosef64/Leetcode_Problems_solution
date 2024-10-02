class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ind = 0
        for x in nums:
            if x != val:
                nums[ind] = x
                ind += 1
        return ind
        