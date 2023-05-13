# [28 해시테이블 디자인]


# 내가 푼 것 - 이렇게 허벌로 풀라는 문제는 아닌듯함.

class Solution:
  def __init__(self):
    self.h = {}
  
  def put(self, key, value):
    self.h[key] = value
  
  def get(self, key):
    if key in self.h: return self.h[key]
    else: return -1
  
  def remove(self, key):
    if key in self.h: del self.h[key]

# 책 풀이 - 개별 체이닝 ? 무슨 말인지 모르겠음.