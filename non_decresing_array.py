class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        nMistake ,tem = 0,[]
        for ind in range(len(nums)-1):
            if nums[ind] > nums[ind+1]:
                if nMistake > 0:
                    return False
                if tem and tem[-1] > nums[ind+1]:
                    nums[ind+1] = nums[ind]
                nMistake += 1
            tem.append(nums[ind])
        return True
        
        
