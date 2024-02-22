class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        Not ,n = set(),len(fronts)
        for ind in range(n):
            if fronts[ind] == backs[ind]:
                Not.add(fronts[ind])
        ans = float("inf")
        for ind in range(n):
            if fronts[ind] not in Not:
                ans = min(ans,fronts[ind])
            if backs[ind] not in Not:
                ans = min(ans,backs[ind])
        return ans if ans!=float("inf") else 0
