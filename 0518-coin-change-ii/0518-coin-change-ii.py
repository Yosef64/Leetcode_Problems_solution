class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        row = [0 for _ in range(amount+1)]
        row[0] = 1
        for coin in coins:
            for amt in range(coin,amount+1):
                row[amt] += row[amt-coin]
        return row[-1]

            