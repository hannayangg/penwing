# [39 코스 스케줄]

import collections

# 내가 푼 것 -> 개선: 굳이 dic을 삭제 필요 x

def F(num, pre):
  def dfs(course):
    if course not in dic.keys():
      return True

    while dic[course]:
      x = dic[course].pop()
      dfs(x)
    
    if course not in been:
      del dic[course]
      been.add(course)

  dic = collections.defaultdict(list)
  been = set() # 방분한 key 저장
  for v0, v1 in pre:
    dic[v0].append(v1)
  
  for v0,v1 in pre: dfs(v0)
  return not dic



# 책 풀이 - 타임아웃

# been=방문한 코스 저장.
# dfs(c) 이하 두 조건을 통과 시 T. c in been: F & dic[c] F: F

def F(num, pre):
  def dfs(course):
    if course in been: # 조건1
      return False
    been.add(course)

    for x in dic[course]: # 조건2
      if not dfs(x):
        return False
    
    been.remove(course)
    return True

  dic = collections.defaultdict(list)
  been = set()
  for v0, v1 in pre:
    dic[v0].append(v1)

  for x in list(dic):
    if not dfs(x):
      return False
  return True 



# 개선 visited=True인 코스 저장. c in visited: T 

def F(num, pre):
  def dfs(course):
    if course in been:
      return False

    if course in visited: # 조건3
      return True
    
    been.add(course)
    for x in dic[course]:
      if not dfs(x):
        return False
    
    been.remove(course)
    visited.add(course) #
    return True

  dic = collections.defaultdict(list)
  been = set()
  visited = set() #
  for v0, v1 in pre:
    dic[v0].append(v1)

  for x in list(dic):
    if not dfs(x):
      return False
  return True 