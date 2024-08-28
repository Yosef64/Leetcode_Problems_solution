class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.split()
        if not s:return 0
        ans = ''
        for j,i in enumerate(s[0]):
            if j==0 and (i=='-' or i=='+'):
                ans= ans + i if i=='-' else ans
            elif i.isdigit():
                ans+=i
            else:
                break
        if (len(ans)==1 and ans=='-' or ans=='+') or not ans:
            return 0
        elif int(ans)>=2**31:return 2**31-1
        elif int(ans)<-2**31:return -2**31
        return int(ans)
        