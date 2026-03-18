class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniq , ind = 0, 0 
        track = set()
        while ind < len(nums):
            if nums[ind] not in track:
                nums[uniq],nums[ind] = nums[ind], nums[uniq]
                track.add(nums[uniq])
                uniq += 1
            ind += 1
        return uniq
                
