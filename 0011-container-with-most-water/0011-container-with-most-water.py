class Solution:
    def maxArea(self, height: List[int]) -> int:
        temp = 0
        left , right = 0 , len(height) - 1
        while left < right:
            area = min(height[right],height[left])*(right - left)
            temp = max(temp,area)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return temp
                
                