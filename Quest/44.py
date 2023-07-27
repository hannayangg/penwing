# [44. leetcode 143]




class ListNode:
  def __init__(self, val):
    self.val = val
    self.next = None


    
# 오른쪽만 스택에 담는 방법.

def F(head):
  s = head
  f = s.next
  while f and f.next:
    s = s.next
    f = f.next.next
  
  # 스택에 담기
  st = []
  tail = s
  s = s.next
  while s:
    st.append(s)
    s = s.next
  tail.next = None

  # 연결
  crnt = head
  while crnt and st:
    new = st.pop()
    next = crnt.next
    crnt.next = new
    new.next = next
    crnt = next




# 메모리 없는 방법 - 오른쪽 노드 reverse.

def F(head):
  s, f = head, head.next
  while f and f.next:
    s = s.next
    f = f.next.next
  
  # 오른쪽 reverse
  prev = None
  crnt = s.next
  s.next = None
  while crnt:
    next = crnt.next
    crnt.next = prev
    prev = crnt
    crnt = next

  # 연결
  first, second = head, prev
  while first and second:
    tmp1, tmp2 = first.next, second.next
    first.next = second
    second.next = tmp1
    first, second = tmp1, tmp2
