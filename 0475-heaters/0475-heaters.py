class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def binarySearch(num):
            left , right = 0 ,len(heaters) - 1
            while left < right:
                mid = (right - left) // 2 + left
                if heaters[mid] < num:
                    left = mid + 1
                elif heaters[mid] > num:
                    right = mid - 1
                else:
                    return mid
            return left
        ans = 0
        # print(heaters,houses)
        for num in range(len(houses)):
            pos = binarySearch(houses[num])
            # print(pos)
            if heaters[pos] >= houses[num]:
                left = abs(houses[num] - heaters[pos - 1]) if pos else float("inf")
                right = heaters[pos] - houses[num]
            else:
                left = houses[num] - heaters[pos]
                right = abs(heaters[pos+1] - houses[num]) if pos < len(heaters)-1 else float("inf")
                
            # print(left,right)
            ans = max(ans,min(left,right))
        return ans