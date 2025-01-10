class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums) - 2):
            for inx in range(i +1,len(nums) - 1):
                l,r = inx +1, len(nums) - 1
                target = nums[i] + nums[inx]
                while l < r:
                    mid = (r - l) // 2 + l
                    # print(mid)
                    if target > nums[mid]:
                        l = mid + 1
                    else:
                        r = mid - 1
        
                res += (l - inx) - int(target <= nums[l])
        return res
                

        