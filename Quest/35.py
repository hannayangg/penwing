# [35. leetcode 56]


def F(arr):
  arr.sort()
  res = []
  for i in range(len(arr)):
    l, r = arr[i]
    if res and res[-1][1] >= arr[i][0]:
      v0, v1 = res.pop()
      l = min(l, v0)
      r = max(r, v1)
    res.append([l, r])
  return res



def F(arr):
  arr.sort()
  res = []
  pre = arr[0]
  for i in range(1, len(arr)):
    # pre값이 구간밖 - 저장
    if pre[1] < arr[i][0]:
      res.append(pre)
      pre = arr[i]
      continue
    # pre값이 구간안 - 업데이트
    pre[0] = min(pre[0], arr[i][0])
    pre[1] = max(pre[1], arr[i][1])
    
  return res + [pre]