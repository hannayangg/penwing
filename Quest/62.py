# [62. leetcode 102]


def F(root):
  if not root: return None
  q = [root]
  res = []

  while q:
    tmp = []
    
    for _ in range(len(q)):
      node = q.pop(0)
      tmp.append(node.val)
      if node.left: q.append(node.left)
      if node.right: q.append(node.right)
    
    res.append(tmp)
  return res