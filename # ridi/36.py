# [36 조합의 합]

# 내가 푼 것

def F(candidates, target):
  def dfs(com, digit):
    if com == 0:
      result.append(digit)
      return
    elif com < 0: return

    key = digit[-1] if digit else 0
    for x in candidates:
      if x >= key: # 중복 방지
        dfs(com-x, digit+[x])

  result = []
  dfs(target, [])
  return result


# 책 풀이
# dfs 인자를 하나 늘려서 중복 방지

def F(candidates, target):
  def dfs(com, idx, digit):
    if com == 0:
      result.append(digit)
      return
    elif com < 0: return

    for i in range(idx, len(candidates)):
      dfs(com - candidates[i], i, digit+[candidates[i]])
  
  result = []
  dfs(target, 0, [])
  return result