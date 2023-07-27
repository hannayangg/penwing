# [40. leetcode 141]


# 셋

def F(head):
  s = set()
  while head:
    if head in s:
      return True
    s.add(head)
    head = head.next
  return False



# O(1)메모리 - slow, fast 포인터

def F(head):
  slow = fast = head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      return True
  return False