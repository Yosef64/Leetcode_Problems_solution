class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        n=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==target:
                n.append(i)
        return n
                
        