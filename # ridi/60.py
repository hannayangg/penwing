# [60 삽입 정렬 리스트]
class ListNode:
  def __init__(self, val):
    self.val = val
    self.next = None

# 내가 푼 것
# 삽입할 곳: 더미노드에서 시작하여 적당한 곳 찾아 이동.

def F(root):
  dummy = ListNode(0)
  dummy.next = root
  past = root
  while past and past.next:
    node = past.next
    if node.val < past.val:
      left = dummy
      while left.next.val < node.val:
        left = left.next
      node.next, left.next, past.next = left.next, node, node.next
    else:
      past = past.next
  return dummy.next



# 책 풀이
# 더미노드 2개 (더미1 = 정렬하며 이동 & 더미2 = 이동한 더미를 처음으로)


def F(head):
  cur = parent = ListNode(None) # 더미 2개
  while head:

    while cur.next and cur.next.val < head.val:
      cur = cur.next

    cur.next, head.next, head = head, cur.next, head.next
    cur = parent

  return cur.next

# cur = parent = None 한 줄에 써야하는 이유.
# cur이 만든 연결이 parent에도 공유되기 때문.

# None(c=p) - 2    - 4
# None(p)   - 2(c) - 4
# None(c=p) - 2    - 4