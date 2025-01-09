class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count , n_p = 0, len(pref)
        for word in words:
            if word[:n_p] == pref:
                count += 1
        return count