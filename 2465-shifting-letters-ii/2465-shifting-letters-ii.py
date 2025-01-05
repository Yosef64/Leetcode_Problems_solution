class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pre = [0] * (len(s) + 1)
        words = list(s)
        for s,e,d in shifts:
            if d:
                pre[s], pre[e+1] = pre[s] + 1,pre[e+1] - 1
            else:
                pre[s], pre[e+1] = pre[s] - 1,pre[e+1] + 1
        pre_sum = 0
        for ind in range(len(words)):

            pre_sum += pre[ind]
            word_val = ord(words[ind]) - 97 + pre_sum
            words[ind] = chr(word_val % 26 + 97)

        return "".join(words)
