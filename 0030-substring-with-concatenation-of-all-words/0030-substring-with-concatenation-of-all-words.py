class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        count , wLen = Counter(words) , len(words[0])
        print(wLen)
        ans = []
        @cache
        def check(st):
            f , temp = 0 , Counter()
            while f < len(st):
                t = st[f:f+wLen]
                temp[t] += 1
                if temp[t] > count[t]:
                    return False
                f += wLen
            return True
                
        l = 0
        for r in range(wLen*len(words),len(s)+1):
            con = check(s[l:r])
            if con:
                ans.append(l)
            l += 1
        return ans