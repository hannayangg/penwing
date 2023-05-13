# [08 빗물 트래핑]


# 단순함

def F(arr):
  # maxL : i 인덱스에서 왼쪽 장벽 최댓값
  # maxR : i 인덱스에서 오른쪽 장벽 최댓값
  maxL, maxR = [], []
  tmp = 0
  for i in range(len(arr)):
    maxL.append(tmp)
    if tmp < arr[i]:
      tmp = arr[i]
  tmp = 0
  for i in range(len(arr)-1, -1, -1):
    maxR.append(tmp)
    if tmp < arr[i]:
      tmp = arr[i]
  maxR.reverse()
  
  # 쌓인 빗물 : 두 장벽 중 작은 것 - i 값
  res = 0
  for i in range(len(arr)):
    tmp = min(maxL[i], maxR[i]) - arr[i]
    if tmp > 0: res += tmp
  return res








# 투 포인터로 할 경우
# 해당 i 인덱스에서 정확한 maxL, maxR 모르는데도 풀리지?



# 책 풀이

def F(arr):
  l, r = 0, len(arr)-1
  maxleft, maxright = arr[l], arr[r]
  res = 0

  while l < r:
    leftmax = max(leftmax, arr[l])
    rightmax = max(rightmax, arr[r])

    if maxleft < maxright:
      res += maxleft - arr[l]
      l += 1
    else:
      res += maxright - arr[r]
      r -= 1
  return res



# 니트코드 - 책 풀이와 동일
def F(arr):
  l, r = 0, len(arr)-1
  leftmax, rightmax = arr[l], arr[r]
  res = 0

  while l < r:
    if leftmax < rightmax:
      l += 1
      leftmax = max(leftmax, arr[l])
      res += leftmax - arr[l]
    else:
      r -= 1
      rightmax = max(rightmax, arr[r])
      res += rightmax - arr[r]
  return res