# [17. leetcode 300]


# Bottom up
# dp[i] = max(dp[i], 1 + dp[j])


def F(nums):
  dp = [1] * len(nums)

  for i in range(1, len(nums)):
    for j in range(i):
      if nums[j] < nums[i]:
        dp[i] = max(dp[i], 1 + dp[j])
  return max(dp)
