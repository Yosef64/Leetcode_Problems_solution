class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x:x[0])
        def fn(val,dic):
            for k in dic:
                if dic[k] <= val:
                    return [k]
            return []
        dic , ans = {x:0 for x in range(n)},defaultdict(int)
        arr = []
        for f,s in meetings:
            res = fn(f,dic)
            if res:
                dic[res[0]] = s
                ans[res[0]] += 1
                heapq.heappush(arr,s)
                continue
            ele = heapq.heappop(arr)
            for k in dic:
                if dic[k] == ele:
                    dic[k] = dic[k] + s-f if ele !=0 else s
                    heapq.heappush(arr,dic[k])
                    ans[k] += 1
                    break
        maxE = 0
        for k in ans:
            if ans[maxE] < ans[k]:
                maxE = k
        return maxE