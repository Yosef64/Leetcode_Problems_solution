class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ls=[]
        n=len(arr)
        while sorted(arr)!=arr:
            maxi=max(arr[0:n])
            maindex=arr.index(maxi)
            if maindex!=0:
                arr[0:maindex+1]=reversed(arr[0:maindex+1])
                ls.append(len(arr[0:maindex+1]))
            arr[0:n]=reversed(arr[0:n])
            ls.append(len(arr[0:n]))
            n-=1
        return ls
        