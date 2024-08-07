class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dic = defaultdict(int)
        def fn(ind , cur_sum):
            if ind >= n or cur_sum <= 0:
                return cur_sum == 0
            state = (ind,cur_sum)
            if state not in dic:
                dic[state] = fn(ind+1,cur_sum - nums[ind]) or fn(ind+1,cur_sum)
            return dic[state]
        return sum(nums)%2 == 0 and fn(0,sum(nums)//2)
            
        