# [15 연결리스트 뒤집기]

class ListNode:
  def __init__(self, val):
    self.val = val
    self.next = None

# 내가 푼 방법 - 다중할당으로 방향 바꿈
def F(head):
  crnt = head
  rev = None
  while crnt:
    rev, crnt.next, crnt = crnt, rev, crnt.next
  return rev


# 책 풀이 - 반복 & 재귀

def F(head):
  node, prev = head, None
  while node:
    next, node.next = node.next, prev # 다중할당 방향 바꿈
    node, prev = next, node # 이동
  return prev


# 반복 풀이 -> 재귀 풀이
# prev = None -> 함수 파라미터 설정
# node, prev = next, node -> reverse(next, node) 호출

def F(head):
  def reverse(node, prev=None):
    if not node:
      return prev
    next, node.next = node.next, prev
    return reverse(next, node)
  return reverse(head)