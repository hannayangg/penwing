# [26 원형 데크 디자인]
# 더블리링크드리스트 이용. 헤드와 테일이 있고, left right 두 방향으로 연결.
# 코드없는 프로그래밍 큐 소개 부분 참고할 것.
 
class QueueNode:
  def __init__(self, val):
    self.val = val
    self.right = None
    self.left = None

class Queue:
  def __init__(self,k):
    self.head = QueueNode(0)
    self.tail = QueueNode(0)
    self.head.right = self.tail
    self.tail.left = self.head
    self.k = k
    self.len = 0
  

  def _add(self, node, new):
    n = node.right
    node.right = new
    new.left = node
    new.right = n
    n.left = new
  
  def insertFront(self, val):
    if self.len == self.k: return False
    self.len += 1
    self._add(self.head, QueueNode(val))
    return True
  
  def insertLast(self, val):
    if self.len == self.k: return False
    self.len += 1
    self._add(self.tail.left, QueueNode(val))
    return True
  

  def _del(self, node):
    n = node.right.right
    node.right = n
    n.left = node

  def deleteFront(self):
    if self.len == 0: return False
    self.len -= 1
    self._del(self.head)
    return True

  def deleteLast(self):
    if self.len == 0: return False
    self.len -= 1
    self._del(self.tail.left.left)
    return True


  def getFront(self): return self.head.right.val if self.len else -1
  
  def getRear(self): return self.tail.left.val if self.len else -1

  def isEmpty(self): return self.len == 0
  
  def isFull(self): return self.len == self.k

