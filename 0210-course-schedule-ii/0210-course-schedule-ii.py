class Solution:
    def findOrder(self, n: int, p: List[List[int]]) -> List[int]:
        h = {x:[] for x in range(n)}
        
        for f,s in p:
            h[f].append(s)
        print(h)
        v = set()
        ans = []
        def fn(t):
            if t in v:
                return False
            if h[t]==[]:
                if t not in ans:
                    ans.append(t)
                return True
            v.add(t)
            for e in h[t]:
                if fn(e)==0:return 0

            if t not in ans:
                ans.append(t)
            v.remove(t)
            h[t] = []
            
            return True
        for k in h:
            if not fn(k):return []
        
        return ans
        