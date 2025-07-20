from typing import List
class Solution:
    def splitArray(self,nums: List[int], k: int) -> int:
        
        """
        Splits an array into k non-empty subarrays to minimize the largest subarray sum.

        Args:
        nums: A list of integers.
        k: The number of subarrays to split into.

        Returns:
        The minimized largest sum of the split.
        """

        def can_split(largest_sum: int) -> bool:
            """
            Checks if the array can be split into k or fewer subarrays,
            with no subarray sum exceeding largest_sum.
            """
            subarray_count = 1
            current_sum = 0
            for num in nums:
                if current_sum + num > largest_sum:
                    # Start a new subarray
                    subarray_count += 1
                    current_sum = num
                else:
                    current_sum += num
            return subarray_count <= k

        # The search range for the answer
        # The minimum possible largest sum is the max element in nums.
        # The maximum possible largest sum is the sum of all elements.
        low = max(nums)
        high = sum(nums)
        result = high

        while low <= high:
            mid = (low + high) // 2
            
            # If we can split the array with mid as the largest sum
            if can_split(mid):
                # Try for a smaller largest sum
                result = mid
                high = mid - 1
            else:
                # Need to allow a larger sum
                low = mid + 1
                
        return result
            