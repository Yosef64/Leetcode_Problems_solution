class Solution:
    def minSwaps(self, s: str) -> int:
        st = []
        for char in s:
            if st and (char == ']' and st[-1] == '['):
                st.pop()
            else:
                st.append(char)
        count = 0
        for char in st:
            if char == ']':
                count +=  1
                continue
            break
        # print(st)
        return math.ceil(count/2)


        
        