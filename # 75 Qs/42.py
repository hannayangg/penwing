# [42. leetcode 23]



# BF - 2개씩 병합 반복 - 느림


class ListNode:
  def __init__(self, val):
    self.val = val
    self.next = None

# 병합정렬

def F(lists):
  if not lists: return None

  # 분할
  if len(lists)==1:
    return lists[0]
  m = len(lists)//2
  l = F(lists[:m])
  r = F(lists[m:])
  
  # 병합
  dummy = ListNode(0)
  crnt = dummy
  while l and r:
    if l.val < r.val:
      crnt.next = l
      l = l.next
    else:
      crnt.next = r
      r = r.next
    crnt = crnt.next
  while l:
    crnt.next = l
    l = l.next
    crnt = crnt.next
  while r:
    crnt.next = r
    r = r.next
    crnt = crnt.next
  return dummy.next




# 다른 방법: 앞에서부터 2개씩 합치기