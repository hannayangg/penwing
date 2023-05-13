# [35 조합]

# 내가 푼 것

def F(n, k):
  def dfs(idx, digit):
    if idx == k:
      result.append(digit)
      return
    key = digit[-1] if digit else 0
    for x in range(key+1, n+1): # 중복방지
      dfs(idx+1, digit+[x])

  result = []
  dfs(0, [])
  return result




# 책 풀이

def F(n, k):
  def dfs(elements, start, k):
    if k == 0:
      result.append(elements[:])
      return
    for i in range(start, n+1):
      elements.append(i)
      dfs(elements, i+1, k-1) # 중복 방지
      elements.pop() # element 초기화
  
  result = []
  dfs([], 1, k)
  return result


# element i를 넣고 재귀호출 후, 다시 뺌 -> 다음 i 에 영향을 주지 않기 위함.

# for i 다음 세 줄을
# dfs(digit+[i], i+1, k-1) 로 바꾸면 내 풀이랑 같음.