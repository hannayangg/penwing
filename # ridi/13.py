# [13 팰린드롬 연결리스트]

# 내가 푼 것
# 리스트랑 다른 방식이 생각이 안남..
class Solution:
  def F(self, head):
    st = []
    crnt = head
    while crnt:
      st.append(crnt.val)
      crnt = crnt.next
    while len(st) > 1:
      if st.pop(0) != st.pop():
        return False
    return True



# 런너 이용: slow 런너 중앙에 위치
# 역방향 리스트: 더미노드 만들어 다중할당
# 중앙 기준 오른쪽(기존) 왼쪽(rev) 비교

def F(head):
  fast = slow = head
  rev = None # 더미노드

  while fast and fast.next:
    fast = fast.next.next
    rev, rev.next, slow = slow, rev, slow.next
  
  if fast:
    slow = slow.next
 
  while slow:
    if slow.val != rev.val:
      return False
    slow, rev = slow.next, rev.next
  
  return True

  # while rev and rev.val == slow.val:
  #   slow, rev = slow.next, rev.next
  
  # return not rev (rev가 끝인 None까지 도달해야 True)