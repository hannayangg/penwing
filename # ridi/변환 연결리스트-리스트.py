# [리스트 -> 연결리스트]

class ListNode:
  def __init__(self, val):
    self.val = val
    self.next = None


# [연결리스트 -> 리스트]

# 1) 뒤집힌 연결리스트를 만드는 방식 [1,2,3] => 3 -> 2 -> 1
def makeLinkedList(lst):
    prev = None
    for x in lst:
      node = ListNode(x)
      node.next = prev
      prev = node
    return prev

# 2) 제대로된 방법 [1,2,3] => 1 -> 2 -> 3 
def createList(lst):
  if len(lst) == 0:
    return None

  head = ListNode(lst[0])
  prev = head
  
  for i in range(1, len(lst)):
    node = ListNode(lst[i])
    prev.next = node
    prev = node

  return head