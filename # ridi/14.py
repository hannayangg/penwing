# [14 연결리스트 병합]

class ListNode:
  def __init__(self, val):
    self.val = val
    self.next = None


# 내가 푼 것

def F(list1, list2):
  if not list1 or not list2:
    return list1 or list2

  l, r = list1, list2
  dummy = ListNode(0)
  crnt = dummy
  while l and r:
    if l.val > r.val:
      l, r = r, l
    crnt.next = l 
    l = l.next
    crnt = crnt.next # 여기서 다중할당이 안되는 이유 모르겠음
  if r:
    crnt.next = r
  return dummy.next


# crnt.next, crnt = l, crnt.next (x)
# crnt.next 가 앞에서 l로 할당이 되었으므로 이동이 가능
# 맨 앞 crnt.next가 정의되지 않으므로 오류





# 책 풀이
# l, r 순서로 정렬하여 l을 리턴, l.next = F(l.next, r) 연결
# 즉, l.next 와 r 중 작은 값이 연결됨

def F(l, r):
  if not l or not r:
    return l or r
  if l.val > r.val:
    l, r = r, l
  l.next = F(l.next, r)
  return l
