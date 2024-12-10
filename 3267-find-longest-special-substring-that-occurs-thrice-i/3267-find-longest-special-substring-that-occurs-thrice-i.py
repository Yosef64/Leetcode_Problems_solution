class Solution:
    def maximumLength(self, s: str) -> int:
       
        res, count = -1, defaultdict(int)
        n , l = len(s) ,0
        for r in range(n):
            if r and s[l] != s[r]:
                l = r
            w = s[l:r+1]
           
            for i in range(len(w)):
                wr  = w[:i+1]
                count[wr] += 1
                if count[wr] >= 3 and len(wr) > res:
                    res = i + 1

        return res
