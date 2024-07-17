class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = defaultdict(int)
        l , ans = 0 , 0
        for i in range(len(s)):
            while window[s[i]]:
                window[s[l]] -= 1
                l += 1
            window[s[i]] += 1
            ans = max(ans,i - l + 1)
        return ans
        