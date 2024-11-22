class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        pattern_counts = Counter()
    
        for row in matrix:
            # Compute the canonical pattern and its complement
            canonical = tuple(row)
            complement = tuple(1 - cell for cell in row)
            
            # Increment count for the canonical pattern
            pattern_counts[canonical] += 1
            pattern_counts[complement] += 1
        
        # Return the maximum count of identical rows
        return max(pattern_counts.values())