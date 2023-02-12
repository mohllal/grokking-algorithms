def knapsack(weight, weights, values, n):
    dp = [[0 for _ in range(weight + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, weight + 1):
            if weights[i - 1] <= w:
              prev = dp[i - 1][w]
              curr = values[i - 1] + dp[i - 1][w - weights[i - 1]]
              dp[i][w] = max(prev, curr)
            else:
              dp[i][w] = dp[i - 1][w]
 
    return dp[n][weight]

if __name__ == "__main__":
  values = [60, 100, 120]
  weights = [10, 20, 30]
  weight = 50

  print("knapsack items' value:", knapsack(weight, weights, values, len(values)))