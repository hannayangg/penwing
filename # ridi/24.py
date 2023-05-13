# [24 스택을 이용한 큐 구현]

# 내가 푼 것
# 모르는 것 push: pop()이랑 append()만 이용할 수 있나? 안될듯
class MyQueue:
  def __init__(self):
      self.st = []

  def push(self, x: int) -> None:
      tmp = [x]
      self.st = tmp + self.st
      # self.st.insert(0, x) 도 되긴 함.

  def pop(self) -> int:
      return self.st.pop()

  def peek(self) -> int:
      return self.st[-1]


# 책 풀이 - 스택 2개 사용.
# 담을 때 input에 담고,
# 리턴할 때 input 값들 다 빼서 거꾸로 output에 옮겨담음)

class MyQueue:
  def __init__(self):
    self.input = []
    self.output = []

  def push(self, x):
    self.input.append(x)

  def peek(self): ###
    if not self.output:
      while self.input:
        self.output.append(self.input.pop())
    return self.output[-1]

  def pop(self):
    self.peek()
    return self.output.pop()
  
  def empty(self):
    return not self.input and not self.output