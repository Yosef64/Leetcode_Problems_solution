class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        buses = defaultdict(list)
        for b in range(len(routes)):
            for r in routes[b]:
                buses[r].append(b)
        q = deque([[source,0]])
        vBus,vRoute = set(),set([source])
        
        while q:
            route , n_bus = q.popleft()
            if route == target:
                return n_bus
            for bus in buses[route]:
                if bus in vBus:
                    continue
                for r in routes[bus]:
                    if r in vRoute:continue
                    q.append([r,n_bus+1])
                    vRoute.add(r)
                vBus.add(bus)
        return -1

        