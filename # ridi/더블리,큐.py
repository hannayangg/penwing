# doubly linked list 로 큐 만들기

# head = 1 = 3 = 5 = 7 = 9 = tail
# dequeue: head = 3 연결
# enqueue: 새로운 노드(2) 만든 후, 9 = 2 = tail 연결

# 새로운 노드 만드는 함수 / 왼쪽과 오른쪽 연결 방향 있음
class QueueNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

class Queue:
  # 초기화
  # head(0) = tail(0) head와 tail노드를 만든 후, 연결
  def __init__(self):
    self.head = QueueNode(0)
    self.tail = QueueNode(0)
    self.head.right = self.tail
    self.tail.left = self.head
  
  def enqueue(self, val):
    new_node = QueueNode(val)
    last_node = self.tail.left

    last_node.right = new_node
    new_node.left = last_node

    new_node.right = self.tail
    self.tail.left = new_node

  def dequeue(self):
    first_node = self.head.right # 삭제할 첫 노드
    if first_node == self.tail: # 첫 노드가 테일 노드라면 (큐에 값이 없다는 뜻) None리턴
      return None
    
    value = first_node.val # 삭제할 첫 노드의 값 (이 값을 리턴)

    second_node = first_node.right
    self.head.right = second_node
    second_node.left = self.head
    
    return value
    


q = Queue()
q.enqueue(1)
q.enqueue(3)
q.enqueue(5)
q.enqueue(7)
q.enqueue(9)

print(q.dequeue(), end = ' ')
print(q.dequeue(), end = ' ')
print(q.dequeue(), end = ' ')
print(q.dequeue(), end = ' ')
print(q.dequeue(), end = ' ')