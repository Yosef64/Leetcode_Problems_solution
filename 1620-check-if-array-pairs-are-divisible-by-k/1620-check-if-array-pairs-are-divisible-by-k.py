class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        dic = defaultdict(int)
        # for num in arr:
        #     dic[-num%k] += 1
        count = 0
        for num in arr:
            if dic[num%k]:
                dic[num%k] -= 1
                count += 1
            else:
                dic[-num%k] += 1
        # print(count)
        return count == len(arr) // 2