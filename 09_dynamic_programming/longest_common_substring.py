def longest_common_substring(str1, str2):
  n = len(str1) + 1
  m = len(str2) + 1

  dp = [[0 for _ in range(m)] for _ in range(n)]

  maximum = 0
  for i in range(n):
    for j in range(m):
      if i == 0 or j == 0:
        dp[i][j] = 0
      elif str1[i - 1] == str2[j - 1]:
        dp[i][j] = dp[i - 1][j - 1] + 1
        maximum = max(maximum, dp[i][j])
      else:
        dp[i][j] = 0

  return maximum

if __name__ == "__main__":
  str1 = "Fishs"
  str2 = "Hishs"

  print("longest common substring:", longest_common_substring(str1, str2))