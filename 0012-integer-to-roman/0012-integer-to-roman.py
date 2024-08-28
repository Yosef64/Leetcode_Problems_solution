class Solution:
    def intToRoman(self, num: int) -> str:
        dic = {
            1:'I',
            5:'V',
            10:'X',
            50:'L',
            100:"C",
            500:"D",
            1000:'M'
        }
        small , large,ans = 1,10,''
        while num > 0:
            t = num % 10
            if t >= 5:
                ans = dic[small] + dic[large] + ans if t + 1 == 10 else dic[5 * small] + dic[small] * (t-5) + ans
            else:ans = dic[small] + dic[5 * small] + ans if t + 1 == 5 else dic[small] * t + ans
            large , small = large * 10 , small * 10
            num //= 10
        return ans
                