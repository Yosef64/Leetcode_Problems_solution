class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst=nums1+nums2
        lst.sort() 
        if len(lst)%2==0:
            n = len(lst)//2
            return (lst[n]+lst[n-1])/2
        
        n=(len(lst)-1)//2
        return lst[n]
            
        