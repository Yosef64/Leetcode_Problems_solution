class Solution:
    def minSwaps(self, s: str) -> int:
        st , count = [] , 0
        for char in s:
            if st and (char == ']' and st[-1] == '['):
                st.pop()
            else:
                count = count + 1 if char == ']' else count
                st.append(char)
        # print(count)
        return math.ceil(count/2)


        
        