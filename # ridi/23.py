# [23 큐를 이용한 스택 구현]

# 내가 푼 것: 이게 맞나?

class MyStack:
  def __init__(self):
    self.q = []

  def push(self, x):
    self.q.append(x)

  def pop(self):
    if self.q:
      idx = len(self.q)-1
      tmp = self.q[idx]
      del self.q[idx]
      return tmp

# 다시 푼 것: append(), q[0], popleft() 만 이용
# pop, top 함수만 조금 바꿈

import collections
class MyStack:
  def __init__(self):
    self.q = collections.deque()

  def pop(self):
    tmp = collections.deque()
    while self.q:
      if len(self.q) == 1:
        res = self.q[0]
        break
      p = self.q.popleft()
      tmp.append(p)
    self.q = tmp
    return res


# 책풀이 - push가 핵심
# 애초에 push 할 때 정렬함 -> pop, top할 때 맨 앞에것 꺼냄
class MyStack:
  def __init__(self):
    self.q = collections.deque()
  
  def push(self, x): ###
    self.q.append(x)
    for _ in range(len(self.q)-1):
      v = self.q.popleft()
      self.q.append(v)
  
  def pop(self):
    return self.q.popleft()
  def top(self):
    return self.q[0]