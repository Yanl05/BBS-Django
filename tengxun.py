#coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
# import sys
# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))

class Solution(object):
    def one(self, coins, amount):
        # dp = [0] + [-1] * amount
        # for x in range(amount):
        #     if dp[x] < 0:
        #         continue
        #     for c in coins:
        #         if x + c > amount:
        #             continue
        #         if dp[x + c] < 0 or dp[x + c] > dp[x] + 1:
        #             dp[x + c] = dp[x] + 1
        # return dp[amount]
        coins.sort(reverse=True)
        self.result = float('inf')

        def dfs(largest_coin, remainder, used_coins):
            if remainder == 0:
                self.result = min(self.result, used_coins)
            for i in range(largest_coin, len(coins)):
                if remainder >= coins[i] * (self.result - used_coins):
                    break
                if coins[i] <= remainder:
                    dfs(i, remainder - coins[i], used_coins + 1)

        dfs(0, amount, 0)

        return self.result if self.result != float('inf') else -1


coins = [i for i in range(1, 7)]


print(Solution().one(coins, 7))