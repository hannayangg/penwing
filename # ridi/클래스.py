# 클래스 안에서 재귀함수

class math:
### __init__ 함수를 꼭 만들지 않아도 됨

  def 팩토리얼(self, n):
    if n <= 1:
      return 1
    else:
      return n * self.팩토리얼(n-1) 

### 클래서 안에서 정의된 함수는 클래스 내 함수니까
### 그냥 함수를 호출하는 게 아니라 클래스의 함수(self.함수)를 호출해야 함
### 그리고 n이랑 n-1 은 클래스 내에 정의된 원소를 불러오는 게 아니니까
### self.n-1 이 아니라 그냥 n-1이라고 씀

print(math().팩토리얼(5))
