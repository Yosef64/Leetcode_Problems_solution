class Solution(object):
    def countVowelStrings(self, n):
        a, e, i, o, u = 1, 1, 1, 1, 1

        while n > 1:
            o += u
            i += o
            e += i
            a += e
            n -= 1

        return a + e + i + o + u