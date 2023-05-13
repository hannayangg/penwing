# [27. k개 리스트 병합]

class ListNode:
  def __init__(self, val):
    self.val = val
    self.next = None
import heapq


# 힙: 그때그때 최솟값을 팝해주기 때문.
# 힙에 [val, i, 노드] 담기.
# 노드-다음노드 연결 때 쓰임.
# i-중복오류방지용 걍 넣음.


def F(lists):
  heap = []

  # 루트들을 힙에 담기.
  for i in range(len(lists)):
    root = lists[i]
    if root:
      heapq.heappush(heap, (root.val, i, root))

  # 힙에서 뺀 최솟값노드 연결, 최솟값노드의 next를 힙에 담기.
  dummy = crnt = ListNode(0)
  while heap:
    val, idx, node = heapq.heappop(heap)
    crnt.next = node
    crnt = crnt.next
    if node.next:
      heapq.heappush(heap, (node.next.val, idx, node.next))

  return dummy.next