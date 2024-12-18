class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack =[]
        for i,j in enumerate(prices):
            while stack and stack[-1][1] >= j:
                temp=stack[-1][1]-j
                prices[stack[-1][0]]=temp
                stack.pop()
            stack.append((i,j))
        return prices
                
                
        