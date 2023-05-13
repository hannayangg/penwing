# [55 배열의 k번째 큰 요소]

# 내가 푼 것
def F(nums, k):
  return sorted(nums, reverse=True)[k-1]

import heapq
def F(nums, k):
  Heap = []
  while nums: # 개선 1
    v = nums.pop()
    heapq.heappush(Heap, v)
    if len(Heap) > k:
      heapq.heappop(Heap)
  return Heap[0] # 개선 2


# 개선
# 1. while 대신 for n in nums (팝 생략)
# 2. 리턴값 Heap[0] 대신 heappop(Heap)


def F(nums, k):
  Heap = []
  for n in nums:
    heapq.heappush(Heap, n)
    if len(Heap) > k:
      heapq.heappop(Heap)
  return heapq.heappop(Heap)





# 책 풀이
# Heap에 음수로 바꾸어 넣는 방법

def F(nums, k):
  Heap = []
  for n in nums:
    heapq.heappush(Heap, -n)
  for _ in range(k-1):
    heapq.heappop(Heap)
  return -heapq.heappop(Heap)


# heapify 이용

def F(nums, k):
  heapq.heapify(nums)
  for _ in range(len(nums)-k):
    heapq.heappop(nums)
  return heapq.heappop(nums)