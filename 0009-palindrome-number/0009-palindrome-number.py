class Solution:
    def isPalindrome(self, x: int) -> bool:
        xStr = str(x)
        return True if xStr[::-1] == xStr else False
        
