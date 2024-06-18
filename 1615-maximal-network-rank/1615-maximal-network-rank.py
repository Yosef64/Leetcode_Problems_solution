class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        dic = defaultdict(set)
        for a , b in roads:
            dic[a].add(b)
            dic[b].add(a)
        ls = [[key,dic[key]] for key in dic]
        ans = 0
        for f in range(len(ls)):
            for s in range(f+1,len(ls)):
                netRank = len(dic[ls[f][0]]) + len(dic[ls[s][0]]) 
                
                ans = max(ans,netRank -1 if ls[f][0] in dic[ls[s][0]] else netRank)
        return ans
            
        