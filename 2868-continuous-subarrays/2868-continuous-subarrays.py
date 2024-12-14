class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        left = right = 0
        count = 0 

        while right < len(nums):
            freq[nums[right]] += 1
            while max(freq) - min(freq) > 2:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

            count += right - left + 1
            right += 1

        return count