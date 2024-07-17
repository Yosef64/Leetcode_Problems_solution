class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ans , n = 0 , len(costs)
        dic = defaultdict(list)
        for ind, (a , b) in enumerate(costs):
            if a < b:
                dic['a'].append(b-a)
            else:
                dic['b'].append(a-b)
            ans += min(a,b)
        
        dif = len(dic['a']) - len(dic['b'])
        # print(dic,ans)
        if dif == 0:return ans
        temp = sorted(dic['b']) if dif < 0 else sorted(dic['a'])
        # print(temp,dif)
        for ind in range(len(temp) - n//2):
            ans += temp[ind]
        return ans