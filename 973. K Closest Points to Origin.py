class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lst=[]
        final=[]
        for i in range(len(points)):
            distance=sqrt(points[i][0]**2+(points[i][1])**2)
            lst.append((distance,points[i]))
        lst.sort()
        print(lst)
        for _ in range(k):
            final.append(lst[_][1])
        return final