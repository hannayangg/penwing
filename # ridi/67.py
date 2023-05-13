# [67 두 배열의 교집합]

# 내가 푼 것

def F(nums1, nums2):
  res = set()
  for n in nums1:
    if n in nums2:
      res.add(n)
  return res


import bisect
def F(nums1, nums2):
  res = set()
  nums2.sort()
  for n in nums1:
    m = bisect.bisect_left(nums2, n)
    if m < len(nums2) and nums2[m] == n:
      res.add(n)
  return res



# 책 풀이 - 투포인터
def F(nums1, nums2):
  nums1.sort()
  nums2.sort()
  l, r = 0, 0
  res = set()
  while l < len(nums1) and r < len(nums2):
    if nums1[l] < nums2[r]:
      l += 1
    elif nums1[l] > nums2[r]:
      r += 1
    else:
      res.add(nums1[l])
      l += 1
      r += 1
  return res