class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        count = 0
        while x != y:
            lastX , lastY = x & 1 , y & 1
            count += lastX != lastY
            x , y = x >> 1 , y >> 1
        return count
        