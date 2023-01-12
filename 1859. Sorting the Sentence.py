class Solution:
    def sortSentence(self, s: str) -> str:
        temp={}
        final=""
        for c in s.split():
            temp[c[-1]]=c[:-1]
        for i in range(1,len(temp)+1):
            if i==len(temp):
                final=final+temp[f"{i}"]
            else:
                final=final+temp[f"{i}"] + " "
        return final

        