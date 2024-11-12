class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        result = [1]
        ix = [0] * len(primes)

        for i in range(n-1):
            next = float("inf")
            mins = []
            for ind ,val in enumerate(ix):
                nextj = primes[ind] * result[val]

                if nextj < next:
                    mins = [ind]
                    next = nextj
                elif nextj == next:
                    mins.append(ind)
            result.append(next)
            for val in mins:
                ix[val] += 1
        return result[-1]