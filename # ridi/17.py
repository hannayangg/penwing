# [17 노드 스왑]

class ListNode:
  def __init__(self, val):
    self.val = val
    self.next = None


# 내가 푼 것

def F(head):
  if not head: return None  # 예외 처리
  if not head.next: return head
  
  b = head.next
  prev = p = ListNode(0)
  
  while b:
    p.next = b   # 연결 방향 바꿈
    head.next = b.next
    b.next = head
  
    p = head   # 다음 노드로 이동
    if not p.next:
      break
    head = p.next
    b = head.next
  return prev.next




# 책풀이 반복 - 내 풀이보다 정돈됨 (b를 while 안에서 정의 => 예외처리 필요없음)

def F(head):
  prev = p = ListNode(None)
  prev.next = head

  while head and head.next:
    b = head.next     # 연결 방향 바꿈
    head.next = b.next
    b.next = head
    p.next = b

    head = head.next    # 다음 노드로 이동
    p = p.next.next
  return prev.next






# 책풀이 재귀 - 어려움!

def F(head):
  if head and head.next:
    p = head.next
    head.next = F(p.next) ###
    p.next = head
    return p
  return head
  # if문 통과하지 못할 경우 (head = [] or head = [1] -> 걍 head 리턴)