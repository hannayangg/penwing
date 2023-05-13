# [58 연결리스트 정렬]

class ListNode:
  def __init__(self, val):
    self.val = val
    self.next = None

# 내가 푼 것
# 분할: fast, slow 두개 진행 -> 절반 기준 좌우 재귀
# 병합: 새로운 노드 만들면서 합침

def F(root):
  if not root.next:
    return root
  dummy = ListNode(0)
  dummy.next = root
  slow = fast = root
  node = dummy
  while fast and fast.next:
    slow = slow.next
    node = node.next
    fast = fast.next.next
  node.next = None
  
  L = F(root)
  R = F(slow)
  cur = dummy
  while L or R:
    if (not R) or (L and R and L.val <= R.val): # 여기 이상하게 복잡함
      new = ListNode(L.val)
      L = L.next
    else:
      new = ListNode(R.val)
      R = R.next
    cur.next = new
    cur = new
  return dummy.next




# 개선
# 분할: slow 이전 노드를 굳이 만들지 않는 방법.
# 병합: 새로운 노드를 만들지 않고 스왑하는 방법.

def _F(L, R): # 병합
  if L and R:
    if L.val > R.val:
      L, R = R, L
    L.next = _F(L.next, R)
  return L or R

def F(head): # 분할 (좌우 쪼개어 병합하는 함수에 보냄)
  if not (head and head.next): return head

  half, slow, fast = None, head, head
  while fast and fast.next:
    half, slow, fast = slow, slow.next, fast.next.next
  half.next = None
  
  left = F(head)
  right = F(slow)
  
  return _F(left, right)



# 개선
# 리스트->연결리스트: 기존 연결리스트에서 val 만 바꾸면 됨.

def F(head):
  p = head
  lst = []
  while p:
    lst.append(p.val)
    p = p.next
  lst.sort()

  p = head
  for i in range(len(lst)):
    p.val = lst[i]
    p = p.next
  return head