class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        pre , dic = [0] , {'a','e','i','o','u'}
        for ind in range(len(words)):
            con = words[ind][0] in dic and words[ind][-1] in dic
            pre.append(pre[-1] + int(con))
            
        ans = []
        for x,y in queries:
            ans.append(pre[y+1] - pre[x])
        return ans