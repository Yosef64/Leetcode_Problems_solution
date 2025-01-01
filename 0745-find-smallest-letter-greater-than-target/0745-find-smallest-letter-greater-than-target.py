class Solution:
    def nextGreatestLetter(self, let: List[str], target: str) -> str:
        left, right = 0 , len(let) - 1
        while left < right:
            mid = (right - left) // 2 + left
            if let[mid] > target:
                right = mid
            else:
                left = mid + 1
        return let[right] if let[right] > target else let[0]