# [38 일정재구성]


# dfs: True / False 조건 찾기.
# dfs가 False일 경우 백트래킹.

import collections


def F(tickets):
  hash = collections.defaultdict(list)
  for src, dst in sorted(tickets): # 개선: 매번 정렬x.
    hash[src].append(dst)

  res = ["JFK"]
  
  def dfs(src):
    # True 경로.
    if len(res) == len(tickets) + 1: return True
    # False 경로: 나가는 화살표가 없을 경우.
    if src not in hash: return False
    
    for i, v in enumerate(hash[src]):
      hash[src].pop(i)
      res.append(v)
      if dfs(v):
        return True
      # False 경로라면? 백트래킹. 반대로 되돌리기.
      else:
        hash[src].insert(i, v)
        res.pop()

  dfs("JFK")
  return res






# 책풀이

def F(tickets):
  hash = collections.defaultdict(list)
  for v, w in tickets:
    hash[v].append(w)

  res = []
  def dfs(a):
    while hash[a]:
      dfs(hash[a].pop(0))
    res.append(a) # while 건너뛰는 a부터 쌓임.(??)

  dfs("JFK")
  return res[::-1]
