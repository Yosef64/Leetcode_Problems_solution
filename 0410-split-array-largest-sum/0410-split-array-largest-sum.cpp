#include <vector>
#include <numeric>    // For std::accumulate
#include <algorithm>  // For std::max_element

class Solution {
public:
    int splitArray(std::vector<int>& nums, int k) {
        // The helper function checks if we can split the array into 'k' or fewer
        // subarrays, where no subarray sum exceeds the given 'largest_sum'.
        auto canSplit = [&](long long largest_sum) {
            int subarray_count = 1;
            long long current_sum = 0;
            for (int num : nums) {
                if (current_sum + num > largest_sum) {
                    // Start a new subarray if the current one would exceed the limit.
                    subarray_count++;
                    current_sum = num;
                } else {
                    current_sum += num;
                }
            }
            return subarray_count <= k;
        };

        // Set the search range for our binary search.
        // 'low' is the largest single element, as that's the smallest possible answer.
        // 'high' is the total sum of the array, the largest possible answer.
        // We use 'long long' to prevent potential integer overflow with large sums.
        long long low = *std::max_element(nums.begin(), nums.end());
        long long high = std::accumulate(nums.begin(), nums.end(), 0LL);
        
        long long result = high;

        while (low <= high) {
            long long mid = low + (high - low) / 2;
            
            if (canSplit(mid)) {
                // This 'mid' is a potential answer. Let's try for an even smaller sum.
                result = mid;
                high = mid - 1;
            } else {
                // This 'mid' is too small. We need to allow a larger subarray sum.
                low = mid + 1;
            }
        }

        return result;
    }
};