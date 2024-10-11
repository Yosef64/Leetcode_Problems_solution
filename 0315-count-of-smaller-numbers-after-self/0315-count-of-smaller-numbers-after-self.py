from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        srL = SortedList()
        def getMins(t):
            left , right = 0 , len(srL) - 1
            while left <= right:
                mid = (right - left) // 2 + left
                # print(mid)
                if srL[mid] >= t:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        ans = [0] * len(nums)
        for ind in range(len(nums) - 1,-1,-1):
            count = getMins(nums[ind])
            ans[ind] = count
            srL.add(nums[ind])
        return ans



        