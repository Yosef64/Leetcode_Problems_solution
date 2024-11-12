class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        result = [1]
        ix = [0] * len(primes)

        for i in range(n-1):
            curMin = float("inf")
            mins = []
            for ind ,val in enumerate(ix):
                nextj = primes[ind] * result[val]

                if nextj < curMin:
                    mins = [ind]
                    curMin = nextj
                elif nextj == curMin:
                    mins.append(ind)
            result.append(curMin)
            for val in mins:
                ix[val] += 1
        return result[-1]