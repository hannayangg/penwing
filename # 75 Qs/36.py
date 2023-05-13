# [36. leetcode 435]

arr = [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],
 [95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]


# 시간 초과
def S(arr):
  arr.sort()
  def F(arr, count):
    for i in range(1, len(arr)):
      if arr[i-1][1] > arr[i][0]:
        arr1 = arr[:]
        arr2 = arr[:]
        arr1.pop(i)
        arr2.pop(i-1)
        a = F(arr1, count+1)
        b = F(arr2, count+1)
        return min(a, b)
    return count
  return F(arr, 0)


# 겹칠 경우, 이전값과 현재값 중 작은 값을 취해야, res최소화.
# arr[i][1] = min(arr[i-1][1], arr[i][1])

def F(arr):
  arr.sort()
  res = 0
  for i in range(1, len(arr)):
    if arr[i-1][1] > arr[i][0]:
      res += 1
      arr[i][1] = min(arr[i-1][1], arr[i][1])
  return res