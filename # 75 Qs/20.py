# [20. leetcode 39]



# BT 느림.
def S(candidates, target):
  res = []
  def F(com, curSum):
    if com==0 and sorted(curSum) not in res:
      res.append(sorted(curSum))
      return
    if com < 0:
      return
    for c in candidates:
      F(com-c, curSum+[c])
  F(target, [])
  return res


# 개선: 인덱스 범위 제한하여 중복 방지.
def S(candidates, target):
  res = []
  def F(com, i, curSum):
    if com == 0:
      res.append(curSum)
      return
    if com < 0:
      return
    for j in range(i, len(candidates)):
      c = candidates[j]
      F(com-c, j, curSum+[c])
  F(target, 0, [])
  return res
