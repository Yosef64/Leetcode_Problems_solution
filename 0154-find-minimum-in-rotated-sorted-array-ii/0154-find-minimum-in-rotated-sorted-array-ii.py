class Solution:
    def findMin(self, nums: List[int]) -> int:
        left , right = 0 , len(nums) - 1
        def checkInc(l,r):
            for inx in range(l+1,r):
                if nums[inx] < nums[l]:return True
            return False

        while left < right:
            mid = (right-left) // 2 + left
            if nums[mid] < nums[right]:
                right = mid
                print(mid)
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                if checkInc(mid,right):
                    left = mid + 1
                else:
                
                    right = mid
        return nums[right]