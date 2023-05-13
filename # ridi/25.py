# [25 원형 큐 디자인]

# 내가 푼 것
# 단순하게 리스트로 큐 구현함.
# 다른 점은 리스트 크기 k넘어가면 enqueue 못하게 막은것 뿐,,

class Circle:
  def __init__(self, k):
    self.q = []
    self.k = k

  def enqueue(self, value):
    if len(self.q) >= self.k: return False
    self.q.append(value)
    return True

  def dequeue(self):
    if len(self.q) == 0: return False
    self.q.pop(0)
    return True
  
  def Rear(self):
    if len(self.q) == 0: return -1
    return self.q[-1]
  def Front(self):
    if len(self.q) == 0: return -1
    return self.q[0]
  def isFull(self):
    return len(self.q) == self.k
  def isEmpty(self):
    return len(self.q) == 0





# 책 풀이
# 시작과 끝 포인터 지정하고, 인큐 디큐 할 때마다 포인터 이동.
# 큐 사이즈가 k개로 한정되므로, 포인터 이동 후 k로 나눠줌. 

class Circle:
  def __init__(self, k):
    self.q = [None] * k
    self.maxlen = k
    self.p1 = 0 # 시작
    self.p2 = 0 # 끝
  
  def enqueue(self, value):
    if self.q[self.p2]:
      return False
    else:
      self.q[self.p2] = value
      self.p2 = (self.p2 + 1) % self.maxlen
      # 한 칸 이동 후 k로 나눠줌 (k를 넘어가지 않도록)
      return True
  
  def dequeue(self):
    if self.q[self.p1] is None:
      return False
    else:
      self.q[self.p1] = None
      self.p1 = (self.p1 + 1) % self.maxlen
      return True
  
  def isEmpty(self):
    return self.p1 == self.p2 and self.q[self.p1] is None
  
  def isFull(self):
    return self.p1 == self.p2 and self.q[self.p1] is not None
  
  def Front(self):
    return -1 if self.q[self.p1] is None else self.q[self.p1]
  
  def Rear(self):
    return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1]