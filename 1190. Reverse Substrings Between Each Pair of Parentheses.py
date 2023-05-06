class Solution:
    def reverseParentheses(self, s: str) -> str:
        st=[]
        i=0
        while i<len(s):
            if s[i]!=")":
                st.append(s[i])
            else:
                some=[]
                while st[-1]!="(":
                    some.append(st.pop())
                st.pop()
                st.extend(some)
            i+=1
        return "".join(st)