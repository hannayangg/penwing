# [65 이진 검색]

# 내가 푼 것 - 반복

def F(nums, target):
  l, r = 0, len(nums)-1
  while l <= r:
    m = (l+r)//2
    if nums[m] < target:
      l = m+1
    elif nums[m] > target:
      r = m-1
    else:
      break # 개선: return m
  return m if nums[m] == target else -1 # 개선: return -1



# 재귀 - 복잡해서 이상함

def F(nums, target):
  res = 0
  def S(arr, p): # 개선: 인덱스를 변수로 사용.
    if not arr:
      return
    nonlocal res
    l, r = 0, len(arr)-1
    m = (l+r)//2
    if arr[m] < target:
      S(arr[m+1:], p+m+1)
    elif arr[m] > target:
      S(arr[:m], p)
    else:
      res = p + m
      return
  S(nums, 0)
  return res if nums[res] == target else -1