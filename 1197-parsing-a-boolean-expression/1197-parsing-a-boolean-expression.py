class Solution:
    def parseBoolExpr(self, exp: str) -> bool:
        st , ops = [] , []
        dic = {'t':True,'f':False}
        for char in exp:
            
            cur = -1
            while char == ')' and (st and st[-1] != '('):
                ex = st.pop()
                if cur == -1:
                    if ops and ops[-1] =='!':
                        cur = not dic[ex]
                        continue
                    cur = dic[ex]
                else:
                    if ops[-1] == '|':
                        cur = cur or dic[ex]
                    elif ops[-1] == '&':
        
                        cur = cur and dic[ex]

            if cur != -1:
                # print(cur)
                st.pop()
                st.append('t' if cur else 'f')
                ops.pop()
            else:
                if char in ['&','|','!']:
                    ops.append(char)
                elif char in dic or char in ['(',')']:
                    st.append(char)
        return dic[st[0]]
                     