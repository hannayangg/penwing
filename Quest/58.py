# [58. leetcode 104]



def F(node):
  if not node: return 0
  return max(F(node.left), F(node.right)) + 1


# 큐 이용(BFS) 넓게, 레벨을 따짐.

def F(node):
  if not node: return 0
  
  res = 0
  q = [node]
  while q:
    for i in range(len(q)):
      v = q.pop(0)
      if v.left: q.append(v.left)
      if v.right: q.append(v.right)
    res += 1
  return res


# 스택 이용(DFS)

def F(node):
  if not node: return 0
  
  res = 0
  st = [[node, 1]]
  while st:
    v, c = st.pop()
    res = max(res, c)
    if v.left: st.append([v.left, c+1])
    if v.right: st.append([v.right, c+1])
  return res