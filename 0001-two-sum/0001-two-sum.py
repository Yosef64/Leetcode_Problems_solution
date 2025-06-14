class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        ls = []
        for i in range(len(nums)):
            if target-nums[i] in hash:
                ls.append(hash[target-nums[i]])
                ls.append(i)
                return ls
            else:
                hash[nums[i]] = i
        return ls
