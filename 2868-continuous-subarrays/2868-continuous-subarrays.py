class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        q = deque([nums[0]])
        ans = 0
        me,mine = nums[0],nums[0]
        for i in range(1,len(nums)):
            
            while q and (abs(me-nums[i])>2 or abs(mine-nums[i])>2):
                q.popleft()
                if q:
                    me = max(q)
                    mine = min(q)
            ans+=len(q)
            me = max(me,nums[i])
            mine = min(mine,nums[i])
            q.append(nums[i])
        return ans+len(nums)
                
        