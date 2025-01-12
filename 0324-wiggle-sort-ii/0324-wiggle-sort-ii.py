class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr_sort = sorted(nums)
        i , j = 1, len(nums) - 1
        while i < len(nums):
            nums[i] = arr_sort[j]
            i , j = i + 2, j -1
        
        i = 0
        while i < len(nums):
            nums[i] = arr_sort[j]
            i , j = i + 2, j - 1