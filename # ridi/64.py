# [64 원점에서 k번째]

# 내가 푼 것

def F(points, k):
  return sorted(points, key=lambda x: (x[0]**2 + x[1]**2))[:k]



import heapq
# 책 풀이
# 힙 이용: min 힙 = 최솟값부터 pop됨.

def F(points, k):
  heap = []
  for (x, y) in points:
    dist = x ** 2 + y ** 2
    heapq.heappush(heap, (dist, x, y))
  print(heap) # 거리가 작은 순

  res = []
  for _ in range(k):
    (dist, x, y) = heapq.heappop(heap)
    res.append((x, y))
  return res