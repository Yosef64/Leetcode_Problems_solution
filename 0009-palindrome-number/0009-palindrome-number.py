class Solution:
    def isPalindrome(self, x: int) -> bool:
        st=str(x)
        if st[::-1]==st:
            return True
        else:
            return False
        