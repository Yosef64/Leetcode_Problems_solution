from collections import deque
class Solution:
    def integerReplacement(self,n: int) -> int:
        """
        Calculates the minimum number of operations for n to become 1.

        Args:
        n: A positive integer.

        Returns:
        The minimum number of operations.
        """
        if n == 1:
            return 0
        
        queue = deque([(n, 0)])  # Store (number, operations)
        visited = {n}

        while queue:
            current_num, ops = queue.popleft()

            if current_num == 1:
                return ops

            # If n is even
            if current_num % 2 == 0:
                next_num = current_num // 2
                if next_num not in visited:
                    visited.add(next_num)
                    queue.append((next_num, ops + 1))
            # If n is odd
            else:
                # n + 1
                next_num_plus = current_num + 1
                if next_num_plus not in visited:
                    visited.add(next_num_plus)
                    queue.append((next_num_plus, ops + 1))
                
                # n - 1
                next_num_minus = current_num - 1
                if next_num_minus not in visited:
                    visited.add(next_num_minus)
                    queue.append((next_num_minus, ops + 1))
                    
        return -1 # Should not be reached given the problem constraints
            