# [16 연결리스트 합치기]

class ListNode:
  def __init__(self, val):
    self.val = val
    self.next = None

# 내가 푼 것
def F(l, r):
  dummy = ListNode(0)
  dummy.next = l
  while l:
    if r:
      l.val += r.val
      r = r.next
    if l.val >= 10:
      if l.next:
        l.next.val += 1
      else:
        l.next = ListNode(1)
      l.val %= 10
    if not l.next: # r이 더 긴 경우 l끝에 연결. (이부분이 어려웠음)
      l.next = r
      break
    l = l.next
  return dummy.next