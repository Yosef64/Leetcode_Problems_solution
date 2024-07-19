class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        def fn(dif,arr):
            if arr and ((dif < 0 and (arr[-1][1] < 0 or dif+arr[-1][1] >=0 )) or (dif >= 0 and arr[-1][1] >=0)):
                return True
            return False
        arr , n = [] , len(gas)
        for i in range(n):
            dif = gas[i] - cost[i]
            if fn(dif,arr):
                arr[-1][1] += dif
            else:
                arr.append([i,dif])
        t = arr[-1][1]
        for i in range(len(arr)-1):
            t += arr[i][1]
            if t < 0:return -1
        return arr[-1][0] if arr[-1][1] >= 0 else -1
        