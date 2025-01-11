class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) <= k:
            return len(s) == k
        count = Counter(s)
        odd  = 0
        for key in count:
            odd += count[key] % 2
            if odd > k:return False
        return True
            
