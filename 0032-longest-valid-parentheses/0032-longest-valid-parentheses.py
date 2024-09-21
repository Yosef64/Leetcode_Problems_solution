class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st = []
        for pr in s:
            if pr == ')':
                val = 0
                while st and st[-1] not in [')','(']:
                    val += st.pop()
                if st and st[-1] == '(':
                    st.pop()
                    st.append(val+2)
                else:
                    st.append(val)
                    st.append(pr)
            else:
                st.append(pr)
        ans = 0
        count = 0
        for num in st:
            if type(num) == int:
                count += num
            else:
                ans = max(ans,count)
                count = 0
        ans = max(count,ans)
        return ans

        
        