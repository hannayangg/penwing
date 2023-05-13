# [43. leetcode 19]


class ListNode:
  def __init__(self, val):
    self.val = val
    self.next = None


# st에 담은 후 n번 삭제

def F(head, n):
  dummy = ListNode(0)
  dummy.next = head
  crnt = dummy
  st = []
  while crnt:
    st.append(crnt)
    crnt = crnt.next
  for _ in range(n):
    st.pop()
  
  node = st[-1]
  node.next = node.next.next
  return dummy.next

# 제거할 노드가 맨 앞일 경우? => 더미노드 필요.



# 투포인터: l, r포인터의 간격 n!!

def F(head, n):
  dummy = ListNode(0)
  dummy.next = head
  l = r = dummy
  for _ in range(n):
    r = r.next
  while r.next:
    l = l.next
    r = r.next
  l.next = l.next.next
  return dummy.next