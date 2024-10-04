class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total = sum(skill)
        team , ans = total / (len(skill)// 2) , 0
        skill.sort()
        left, right = 0 , len(skill) - 1
        while left < right:
            if skill[left] + skill[right] != team:
                return -1
            ans += (skill[left] * skill[right])
            left , right = left + 1 , right - 1
        return ans
        