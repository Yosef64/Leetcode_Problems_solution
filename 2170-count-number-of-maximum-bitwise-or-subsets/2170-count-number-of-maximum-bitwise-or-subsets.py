class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        pos , maxOr = [0] , 0
        count = 0
        for num in nums:
            for ind in range(len(pos)):
                xor = num | pos[ind]
                print(xor)
                pos.append(xor)
                maxOr = max(maxOr,xor)
        for num in pos:
            if num == maxOr:
                count += 1
        return count
        
