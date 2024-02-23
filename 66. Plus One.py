class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ourD = 0
        for num in digits:
            ourD = ourD*10 + num
        ourD += 1
        # print(ourD)
        ans = deque([])
        while ourD > 0:
            l = ourD%10
            ans.appendleft(l)
            ourD//=10
        return ans
