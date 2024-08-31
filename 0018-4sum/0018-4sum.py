class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        v = set()
        
        ans = []
        for i in range(len(nums)-3):
           
            for ind2 in range(i+1,len(nums)-2):
                target2 = target - (nums[i]+nums[ind2])
                
                start , end = ind2+1,len(nums)-1
                while start < end:
                    lSum = nums[start]+nums[end]
                    # print(target2,su)
                    if lSum == target2:
                        arr = [nums[i],nums[ind2],nums[start],nums[end]]
                        tupleA = (nums[i],nums[ind2],nums[start],nums[end])
                        
                        if  tupleA not in v:
                            ans.append(arr)
                            v.add(tupleA)
                        start += 1
                        end -= 1
                    elif lSum > target2:
                        end -= 1
                    else:
                        start += 1
        return ans
        