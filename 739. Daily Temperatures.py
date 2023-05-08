class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0 for i in range(len(temperatures))]
        stak=[]
        for i in range(len(temperatures)):
            while stak and temperatures[i]>stak[-1][1]:
                temp=i-stak[-1][0]
                s=stak[-1][0]
                ans[s]=temp
                stak.pop()
            stak.append((i,temperatures[i])) 
        return ans   
            