class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        f , s = 0 , 0
        n , m = len(name), len(typed)
        while f < n and s < m:
            if name[f] == typed[s]:
                f , s = f + 1, s+1
            else:
                if s == 0 or typed[s] !=typed[s-1]:return False

                s += 1
       
        for ind in range(s,m):
            if typed[ind] != typed[ind-1]:return False
        return f == n