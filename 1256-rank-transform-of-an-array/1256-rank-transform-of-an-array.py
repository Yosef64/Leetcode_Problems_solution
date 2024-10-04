class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        dic = {val:ind+1 for ind,val in enumerate(sorted(set(arr)))}
        ans = []
        for num in arr:
            ans.append(dic[num])
        return ans