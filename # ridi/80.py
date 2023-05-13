# [80 태스크 스케줄러]

# 내가 푼 것
# MaxHeap - [횟수, 캐릭터] 저장.
# 팝 - 최댓값 & n번 팝.
# 푸시 - [횟수-1, 캐릭터] 푸시.  (팝과정 다 끝낸 후 푸시해서 중복팝 방지)

import heapq, collections

def F(tasks, n):
  # MaxHeap 생성
  hash = collections.Counter(tasks)
  heap = []
  for x in hash:
    heapq.heappush(heap,[-hash[x], x])

  count = 0
  while heap:
    # 팝
    p, k = heapq.heappop(heap)
    count += 1
    
    tmp = []
    for _ in range(n):
      if p+1 == 0: continue  
      if not heap:
        count += 1
        continue
      p1, k1 = heapq.heappop(heap)
      count += 1
      if p1+1:
        tmp.append([p1+1, k1])
    
    # 푸시
    for x in tmp:
      heapq.heappush(heap, x)
    if p+1:
      heapq.heappush(heap, [p+1, k])

  return count





# 책풀이
# most_common에 2개만 남으면 FOR문 2번 반복
# 1개 남으면 FOR문 1번 반복!!

# 모르겠는 점: 왜 tmp가 필요하지?