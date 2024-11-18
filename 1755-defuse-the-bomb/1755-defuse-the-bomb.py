class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        def positive():
            l , r = 1 , k
            res , curSum = [] ,sum(code[1:k+1])
            res.append(curSum)
            while l < len(code):
                curSum -= code[l]
                curSum += code[(r+1)%len(code)]
                res.append(curSum)
                r = (r +1) % len(code)
                l += 1
            return res
        def negative():
            l , r = len(code) + k , 0
            res , curSum = [] ,sum(code[len(code) + k:])
            # print(curSum)
            res.append(curSum)
            while r < len(code) - 1:
                curSum -= code[l]
                curSum += code[r]
                res.append(curSum)
                l = (l +1) % len(code)
                r += 1
            return res
        if k < 0:return negative()

        return positive()

        