class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        lst=[str(c) for c in nums]
        for i in range(len(nums)-1):
            for j in range(i,len(nums)):
                if int(lst[i][0])<int(lst[j][0]):
                    temp=lst[i]
                    lst[i]=lst[j]
                    lst[j]=temp
                elif int(lst[i][0])==int(lst[j][0]):
                    if int(lst[i]+lst[j])<int(lst[j]+lst[i]):
                        temp=lst[i]
                        lst[i]=lst[j]
                        lst[j]=temp
        s=int("".join(lst))
        return str(s)
        