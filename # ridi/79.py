# [79 키에 따른 대기열 재구성]


# MaxHeap!!

# MaxHeap 키가 큰 순. 팝하여 해당 인덱스에 삽입.
# [height, k]에서 k가 인덱스와 관련이 있다!

import heapq
def F(people):
  heap = []
  for h, k in people:
    heapq.heappush(heap, [-h, k])

  res = []
  while heap:
    h, k = heapq.heappop(heap)
    res.insert(k, [-h, k])
  
  return res




# 왜 Heap.
# 순간순간 최소/최댓값을 뽑아낼 수 있어서.

# 왜 MaxHeap.
# 팝되는 순서 [-7,0] -> [-5,0].
# 0번 인덱스에는 키가 큰 [7,0]이 먼저 삽입되고
# [5,0]이 그것을 밀어내고 0번 인덱스를 차지하게됨!
