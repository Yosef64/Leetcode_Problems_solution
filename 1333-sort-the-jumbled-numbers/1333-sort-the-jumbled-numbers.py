class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        digit_map = {ind:val for ind,val in enumerate(mapping)}
        # print(digit_map)
        ans = []
        for num in nums:
            pre , mapped_value = 1 , 0
            if num == 0:mapped_value = digit_map[num]
            org = num
            while num>0:
                left = num%10
                mapped_value = digit_map[left]*pre + mapped_value
                pre,num = pre*10 ,num//10
            ans.append((mapped_value,org))
        ans.sort(key = lambda x :x[0])
        # print(ans)
        return [ele[1] for ele in ans]