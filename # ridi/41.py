# [41 k경유지 내]

import heapq, collections

# 타임아웃

def F(n, k, src, dst, flights):
  dic = collections.defaultdict(list)
  for v0, v1, v2 in flights:
    dic[v0].append((v2, v1))
  minHeap = [(0, 0, src)]

  while minHeap:
    w1, k1, n1 = heapq.heappop(minHeap)
    if n1 == dst:
      break
    for w2, n2 in dic[n1]:
      if k1 < k+1:
        heapq.heappush(minHeap, (w1+w2, k1+1, n2))

  return w1 if n1 == dst else -1



# 니트코드 - 리스트 두 개 이용.
# flights (s, d, p) 에서 (s까지 비용 + p)값 고려해 업데이트

def F(n, k, src, dst, flights):
  price = [float("inf")] * n
  price[src] = 0

  for i in range(k+1):
    tmp = price[:]
    for s, d, p in flights:

      if price[s] == float("inf"): # s까지도 도달 못하면 패스
        continue
      tmp[d] = min(tmp[d], price[s]+p)
    
    price = tmp[:]

  return -1 if price[dst] == float("inf") else price[dst]



  # 주의:
  # price[dst] if price[dst] is not float("inf") else -1 이건 틀림


  # price = [inf, 0, inf]
  # price[dst] is float("inf") ==> F
  # price[dst] == flost("inf") ==> T 엥?