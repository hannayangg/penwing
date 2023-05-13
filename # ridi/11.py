# [11 자신을 제외한 배열의 곱]

# 니트코드
# 자신을 기준으로 왼쪽 곱과 오른쪽 곱 구한 뒤, 서로 곱함

def F(nums):
  # prefix = [1,1,2,6]
  pre = [1] * len(nums)
  for i in range(1, len(nums)):
    pre[i] = pre[i-1] * nums[i-1]

  # postfix = [24,12,4,1]
  post = [1] * len(nums)
  for i in range(len(nums)-2, -1, -1):
    post[i] = post[i+1] * nums[i+1]
    pre[i] *= post[i]

  return pre


# 개선: pre, post 저장하지 않는 방법

def F(nums):
  pre = 1
  res = [1] * len(nums)
  for i in range(len(nums)):
    res[i] *= pre
    pre *= nums[i]

  post = 1
  for i in range(len(nums)-1, -1, -1):
    res[i] *= post
    post *= nums[i]
  
  return res