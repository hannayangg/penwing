# [40 네트워크 지연 시간]

# 니트코드 풀이
# minHeap에 (path, node)저장 -> 항상 path가 작은 값부터 팝됨
# 푸시할 때 (p1+p2, n2)로 누적하는 것이 중요

import heapq, collections

def F(times, n, k):
  edges = collections.defaultdict(list)
  for u, v, w in times:
    edges[u].append((w, v))

  minHeap = [(0, k)]
  visit = set()
  result = 0

  while minHeap:
    w1, n1 = heapq.heappop(minHeap)
    if n1 in visit:
      continue
    visit.add(n1)
    result = w1

    for w2, n2 in edges[n1]:
      if n2 not in visit: ### 이 조건 필요하지 않음. (시간 단축해줄 뿐..)
        heapq.heappush(minHeap, (w2+w1, n2))

  return result if len(visit)==n else -1