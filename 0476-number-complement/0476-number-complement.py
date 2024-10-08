class Solution:
    def findComplement(self, num: int) -> int:
        res, n = 0, 0
        while num:
            # print(num & 1)
            if not num & 1:
                res += 2 ** n
                
            num >>= 1
            n += 1
        
        return res