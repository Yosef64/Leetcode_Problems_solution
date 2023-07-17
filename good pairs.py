class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n=0
        count=Counter(nums)
        for i in count:
            if count[i]>=2:
                s=factorial(count[i])//(factorial(count[i]-2)*2)
                n+=s
        return n