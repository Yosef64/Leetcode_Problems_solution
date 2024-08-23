class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        largest_num = "".join(sorted(map(str, nums), key=LargerNumKey))
        return largest_num if largest_num[0] != "0" else "0"
