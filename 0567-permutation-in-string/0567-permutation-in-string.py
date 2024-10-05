class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sS1 , end = Counter(s1) , len(s1)
        w = Counter(s2[:end-1])
        l = 0
        for r in range(end-1,len(s2)):
            w[s2[r]] += 1
            print(w)
            if w == sS1:
                return True
            w[s2[l]] -= 1
            if not w[s2[l]]:
                del w[s2[l]]
            l += 1
        return False


        