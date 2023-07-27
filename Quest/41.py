# [41. leetcode 21]


# 재귀
def F(l1, l2):
  if not l1 or not l2:
    return l1 or l2
  if l1.val < l2.val:
    l1.next = F(l1.next, l2)
    return l1
  else:
    l2.next = F(l1, l2.next)
    return l2





class ListNode:
  def __init__(self, val):
    self.val = val
    self.next = None

# 반복
def F(l1, l2):
  dummy = ListNode(None)
  crnt = dummy
  while l1 and l2:
    if l1.val < l2.val:
      crnt.next = l1
      l1 = l1.next
    else:
      crnt.next = l2
      l2 = l2.next

  if l1 or l2:
    crnt.next = l1 or l2
  
  return dummy.next