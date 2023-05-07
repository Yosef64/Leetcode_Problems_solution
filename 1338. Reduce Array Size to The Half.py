class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count=Counter(arr)
        lst=[]
        mid=len(arr)/2
        for i in count:
            lst.append((count[i],i))
        lst.sort()
        s,m=0,0
        i=len(lst)-1
        while i<len(lst):
            m+=lst[i][0]
            s+=1
            if m>=mid:
                return s
            i-=1
            