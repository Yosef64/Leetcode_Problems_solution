class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        for ind, ls in enumerate(tasks):
            ls.append(ind)
        
        
        tasks.sort(key=lambda task: task[0])
        n , heap =  len(tasks), []
        cpuTime , i= tasks[0][0], 0
        ans = []
        
        while heap or i < n:
            while i < n and cpuTime >= tasks[i][0]:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2])) 
                i += 1
            
            if not heap:
                cpuTime = tasks[i][0]
            else:
                time, ind = heapq.heappop(heap)
                cpuTime += time
                ans.append(ind)

        return ans