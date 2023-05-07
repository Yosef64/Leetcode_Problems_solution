class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count=Counter(nums)
        n=0
        for i in nums:
            if count[i] and count[i]>=2 and i*2==k:
                count[i]-=2
                n+=1
            elif count[i] and k-i in count and count[k-i] and i*2!=k:
                count[i]-=1
                count[k-i]-=1
                n+=1
        return n