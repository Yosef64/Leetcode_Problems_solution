class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        nMistake = 0
        for ind in range(len(nums)-1):
            if nums[ind] > nums[ind+1]:
                if nMistake > 0:
                    return False
                if ind > 0 and nums[ind-1] > nums[ind+1]:
                    nums[ind+1] = nums[ind]
                nMistake += 1
        return True
        
