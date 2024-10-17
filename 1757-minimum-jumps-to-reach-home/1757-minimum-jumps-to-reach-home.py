class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        que = deque([(0, 0)])
        forbidden = set(forbidden)
        forbidden.add(0)
        upper = max(max(forbidden), x) + a + b
        level = 0
        
        while que:
            for _ in range(len(que)):
                node, prev = que.popleft()
                
                if node == x:
                    return level
                
                if prev != -1 and node-b >= 0 and node-b not in forbidden:
                    que.append((node-b, -1))
                    
                if upper >= node+a and node+a not in forbidden:
                    que.append((node+a, 1))
                    forbidden.add(node+a)
                    
            level += 1
        return -1