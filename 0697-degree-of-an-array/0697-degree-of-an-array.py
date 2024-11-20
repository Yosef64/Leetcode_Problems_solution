class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = {}
        for ind , val in enumerate(nums):
            if val not in count:
                count[val] = [1,ind,ind]
            else:
                count[val] = [count[val][0]+1,count[val][1],ind]
        minLen , minVal = count[nums[0]][-1] - count[nums[0]][1]+1,nums[0]
        for key in count:
            if count[key][0] > count[minVal][0]:
                minVal = key
                minLen = count[key][-1] - count[key][1] + 1
            elif count[key][0] == count[minVal][0]:
                if count[key][-1] - count[key][1] + 1 < minLen:
                    minVal = key
                    minLen = count[key][-1] - count[key][1] + 1
        return minLen