class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        k=[]
        for i in range(len(nums)):
            large=0
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    large+=1
            k.append(large)
        return k
        