# 노드 클래스 만들기
class Node:
  def __init__(self, head, next=None):
    self.head = head
    self.next = next

# 데이터 생성하기
node1 = Node('일번노드')
node2 = Node('이번노드')
node3 = Node(300)
node4 = Node(40)

# 데이터 연결하기
node1.next = node2
node2.next = node3
node3.next = node4

# 데이터 출력하기
node = node1
while node:
  print(node.head)
  # 출력 후 다음으로 넘어가기
  node = node.next


# 새로운 노드를 노드 사이에 추가하기
node5 = Node('새로운노드')

# 노드2랑 3 사이에 넣기
node2.next = node5
node5.next = node3

# 데이터 출력하기
node = node1
while node:
  print(node.head)
  # 출력 후 다음으로 넘어가기
  node = node.next


# 데이터 삭제하기: 노드3삭제 후, 노드5를 노드4에 연결
del node3
node5.next = node4

# 데이터 출력하기
node = node1
while node:
  print(node.head)
  # 출력 후 다음으로 넘어가기
  node = node.next

