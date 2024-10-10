class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def fn(st,end):
            if st == end:
                return [nums[st]]
            
            left = fn(st,(end - st)//2 + st)
            right = fn((end - st)//2 + st + 1,end)
            arr = []
            f ,s = 0 , 0
            while f < len(left) and s < len(right):
                if left[f] < right[s]:
                    arr.append(left[f])
                    f += 1
                else:
                    arr.append(right[s])
                    s += 1
            arr.extend(left[f:])
            arr.extend(right[s:])
            return arr
        return fn(0,len(nums) - 1)
