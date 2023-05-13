# [39. leetcode 206]


# 반복

def F(head):
  prev, crnt = None, head
  while crnt:
    next = crnt.next
    crnt.next = prev
    prev = crnt
    crnt = next
  return prev



# 재귀 - 어려움

def F(head):
  if not head: return None
  
  newHead = head
  if head.next:
    newHead = F(head.next)
    head.next.next = head
  head.next = None
  return newHead