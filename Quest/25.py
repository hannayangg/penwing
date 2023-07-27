# [25. leetcode 55]


# DP: 시간 초과.
def F(nums):
  dp = [False] * len(nums)
  dp[-1] = True
  for i in range(len(nums)-2, -1, -1):
    for j in range(1, nums[i]+1):
      if (i+j < len(dp)) and dp[i+j]:
        dp[i] = True
      if dp[i]: break
  return dp[0]


# greedy: 도착지점을 끝에서 앞으로 옮기기.
def F(nums):
  end = len(nums)-1
  for i in range(len(nums)-1, -1, -1):
    if i + nums[i] >= end:
      end = i
  not end