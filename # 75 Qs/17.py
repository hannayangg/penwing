# [17. leetcode 300]


# Bottom up

def F(nums):
  dp = [1] * len(nums)
  for i in range(1, len(nums)):
    prev = []
    for j in range(i):
      if nums[j] < nums[i]:
        prev.append(dp[j])
    dp[i] = max(prev)+1 if prev else 1
  return max(dp)


# prev없는 방법: 시간초과. (왜지?)
# dp[i] = max(dp[i], dp[j]+1)