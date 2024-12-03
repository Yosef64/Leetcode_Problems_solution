class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:return []
        st,res = [nums[0]], [str(nums[0])]
        for ind in range(1,len(nums)):
            if nums[ind] - 1 == nums[ind-1]:
                res[-1] = f"{st[-1]}->{nums[ind]}"
            else:
                st.append(nums[ind])
                res.append(str(nums[ind])) 
        return res