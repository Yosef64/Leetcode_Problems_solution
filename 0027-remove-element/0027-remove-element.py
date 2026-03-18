class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        same, ind = 0, 0
        while ind < len(nums):
            if nums[ind] != val and nums[same] ==val:
                nums[ind],nums[same] = nums[same],nums[ind]

            if nums[same] != val:same+=1

            ind += 1
        return same