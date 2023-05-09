class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st=[-1]*len(nums1)
        for i in range(len(nums1)):
            m=nums2.index(nums1[i])
            while m<len(nums2):
                if nums2[m]>nums1[i]:
                    st[i]=nums2[m]
                    break
                m+=1
        return st
        