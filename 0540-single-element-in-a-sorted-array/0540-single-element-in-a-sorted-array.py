class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l , r = 0 , len(nums) - 1
        while l < r:
            mid = (r - l) // 2 + l
            if nums[mid - 1] != nums[mid] and nums[mid + 1] != nums[mid]:return nums[mid]
            print(nums[mid],(l,r))

            if (mid % 2 and nums[mid] != nums[mid - 1]) or (not mid%2 and nums[mid]!=nums[mid+1]):
                r = mid - 1 - mid % 2
            else:
                l = mid + 1 + int(not mid % 2)
        return nums[l]
