# [18 홀짝 연결리스트]

class ListNode:
  def __init__(self, val):
    self.val = val
    self.next = None


# 내가 푼 것 (책풀이)
# 홀짝에 따라 다중할당으로 연결 방향 바꾸고, 다음 노드로 이동

def F(head):
  if not head or not head.next:
    return head
  odd = o = head
  even = e = head.next
  while even and even.next:
    odd.next, even.next = odd.next.next, even.next.next
    odd = odd.next
    even = even.next
  odd.next = e
  return o # 그냥 head를 리턴해도 됨