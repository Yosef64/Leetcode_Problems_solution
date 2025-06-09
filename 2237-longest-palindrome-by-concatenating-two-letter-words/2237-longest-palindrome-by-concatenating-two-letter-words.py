class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count , ans = Counter(words),0
        mid = True
        for key in count:
            if count[key] == 0:continue
            rv = key[1] + key[0]
            if key == rv:
                l ,mod = count[key] // 2,count[key] %2
                ans += l * 4 + int(mid and mod) * 2
                if mid and mod:
                    mid = False

            elif rv in count:
                ans += (min(count[key],count[rv]) *4)
                count[rv] = 0
        return ans


        