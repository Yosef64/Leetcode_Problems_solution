class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        '''
        [0,1,4,4,5,7]
            l    r
        '''
        nums.sort()
        left , right = 0 , len(nums) - 1
        res = 0
        while left < right:
            total = nums[left] + nums[right]

            if total > upper or total < lower:
                left = left + 1 if total < lower else left
                right = right- 1 if total > upper else right
            
            else:
                tr,tl,ind = right,left+1,right
                while nums[tr]+nums[left]>=lower and tl<=tr:
                    mid = (tr-tl)//2 + tl
                    # print(nums[mid])
                    if nums[mid]+nums[left]<lower:
                        tl = mid+1
                    else:
                        ind = mid
                        tr = mid-1
            
                res += right-ind+1
                
                left += 1
        return res


