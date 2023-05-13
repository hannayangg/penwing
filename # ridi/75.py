# [75 최대 슬라이딩 윈도우]


# 시간 초과
# nums 슬라이싱, 인덱스 탐색 오래걸리는 듯.

def F(nums, k):
  m = max(nums[:k])
  midx = nums.index(m)
  res = [m]
  l, r = 1, k

  while r < len(nums):
    if r - midx >= k: # 최댓값을 다시 구하는 경우
      new = nums[l:r+1]
      m = max(new)
      midx = new.index(m) + l
    elif m < nums[r]: # 최댓값 업데이트
      m, midx = nums[r], r

    res.append(m)
    l += 1
    r += 1
  return res


# 니트코드
# Decreasing Queue 큰~작은 순으로 정렬할 것.
# r보다 작은 것들은 pop, l범위 바깥인 것 popleft.

import collections

def F(nums, k):
  res = []
  q = collections.deque() # 인덱스 저장.
  l, r = 0, 0
  while r < len(nums):
    while q and nums[q[-1]] < nums[r]: # r보다 작은 것 pop.
      q.pop()
    q.append(r)

    if q[0] < l: # l범위 바깥 popleft.
      q.popleft()

    if (r+1) >= k:
      res.append(nums[q[0]])
      l += 1
    r += 1
  return res


# 책 풀이 - 시간초과임(..)