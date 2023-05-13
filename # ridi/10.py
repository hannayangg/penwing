# [10 배열 파티션 1]

# 내가 푼 것
def F(arr):
  return sum(sorted(arr)[0:-1:2])
  # 책 풀이 -> [::2] 처음부터 끝까지 2개씩 쪼갠다.



# enumerate()이용  => a[i] 가 n으로.

def 리디(a):
  a.sort()
  result = 0
  for i, n in enumerate(a):
    if i % 2 == 0:
      result += n
  return result