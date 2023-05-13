# [19 역순연결리스트2]

class ListNode:
  def __init__(self, val):
    self.val = val
    self.next = None
    


# 내가 푼 것 - 오래걸렸다.
# 연결리스트 뒤집기[반복] 응용
# 뒤집은 부분 앞뒤로 연결이 어려움 (##)

def F(head, m, n):
  dummy = prev = ListNode(0)
  dummy.next = head
  for _ in range(m-1):
    prev, head = prev.next, head.next
  face, tail = prev, head ##
  prev, head = prev.next, head.next

  for _ in range(n-m):
    next = head.next
    head.next = prev
    head, prev = next, head ##
  face.next, tail.next = prev, head
  return dummy.next



# 책 풀이 - 이 부분이 복잡 (##)
# 뒤집은 부분 연결하는 부분이 없어서 간결함

def F(head, m, n):
  root = start = ListNode(None)
  root.next = head
  for _ in range(m-1):
    start = start.next
  end = start.next

  for _ in range(n-m): ##
    tmp, start.next, end.next = start.next, end.next, end.next.next
    start.next.next = tmp
  return root.next