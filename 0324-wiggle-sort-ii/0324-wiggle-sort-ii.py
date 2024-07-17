class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        [1,5,1,1,6,4,3]
        """
        temp , n = sorted(nums) , len(nums)
        ind = n - 1
        for i in range(1,n,2):
            nums[i] = temp[ind]
            ind -= 1
        for i in range(0,n,2):
            nums[i] = temp[ind]
            ind -= 1
        
        
            
        
        