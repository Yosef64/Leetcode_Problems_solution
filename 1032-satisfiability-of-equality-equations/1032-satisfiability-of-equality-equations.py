class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = [ind for ind in range(26)]
        def find(num):
            if num == parent[num]:return num

            return find(parent[num])
        def union(num1,num2):
            pNum1 , pNum2 = find(num1),find(num2)
            parent[pNum1] = pNum2
        
        for eq in equations:
            if eq[1] == "=":
                char1,char2 = ord(eq[0]) - 97 , ord(eq[-1]) - 97
                union(char1,char2)
        for eq in equations:
            if eq[1]=='!':
                char1 , char2 = ord(eq[0]) - 97 , ord(eq[-1]) - 97
                if find(char1) == find(char2):return False
        return True
                
