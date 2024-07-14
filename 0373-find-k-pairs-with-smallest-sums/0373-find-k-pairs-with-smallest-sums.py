class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap , ans = [] , []
        visited , n , n1 = set([(0,0)]) , len(nums1) , len(nums2)
        heapq.heappush(heap,[nums1[0]+nums2[0],[0,0]])
        while k and heap:
            Sum , indexs = heapq.heappop(heap)
            ind0 , ind1 = indexs
            ans.append([nums1[ind0],nums2[ind1]])
            if 0<=ind0 + 1 < n and (ind0 + 1,ind1) not in visited:
                heapq.heappush(heap,[nums1[ind0 + 1]+nums2[ind1],[ind0+1,ind1]])
                visited.add((ind0 + 1,ind1))
            if 0<=ind1+1 < n1 and (ind0 ,ind1+1) not in visited:
                heapq.heappush(heap,[nums1[ind0]+nums2[ind1+1],[ind0,ind1+1]])
                visited.add((ind0,ind1 + 1))
            k -= 1
        return ans
        