class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count , q = Counter(tasks), deque()
        heap , curInt = [-1*count[key] for key in count],0
        heapq.heapify(heap)
        
        while heap or q:
            curInt += 1
            if heap:
                val = heapq.heappop(heap)+1
                if val:q.append([val,curInt+n])
            if not heap and q:
                curInt = q[0][1]
            if q and q[0][1]<=curInt:
                heapq.heappush(heap,q.popleft()[0])
                
            
        return curInt
        
        
        
        