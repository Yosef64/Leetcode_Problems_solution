class Solution:
    def minLength(self, s: str) -> int:
        st = []
        for char in s:
            
            if st and ((char == "B" and st[-1] == 'A') or (char == "D" and st[-1] == 'C')):
                st.pop()
            else:
                st.append(char)
        
        return len(st)
        