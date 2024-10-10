class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums).most_common()
        final_ans=[]
        for i in range(k):
            final_ans.append(count[i][0])
        return final_ans