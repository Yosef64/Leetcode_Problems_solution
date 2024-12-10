class Solution:
    def maximumLength(self, s: str) -> int:
        def check(word):
            for ind in range(len(word) - 1):
                if word[ind] !=word[ind+1]:
                    return False
            return True
        res, count = -1, defaultdict(int)
        n = len(s)
        for r in range(n):
            for l in range(r+1):
                w = s[l:r+1]
                count[w] += 1
                if count[w] >= 3 and r - l + 1 > res and check(w):
                    res = r - l + 1
        # print(count)
        return res
