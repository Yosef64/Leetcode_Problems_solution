class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapp = {ind:val for ind,val in enumerate(mapping)}
        # print(mapp)
        ans = []
        for num in nums:
            pre , alph = 1 , 0
            if num == 0:alph = mapp[num]
            org= num
            while num>0:
                left = num%10
                alph = mapp[left]*pre + alph
                pre,num = pre*10 ,num//10
            ans.append((alph,org))
        ans.sort(key = lambda x :x[0])
        # print(ans)
        return [ele[1] for ele in ans]