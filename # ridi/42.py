# [42 이진 트리의 최대 깊이]


# 내가 푼 것
def S(root):
  def F(node):
    if not node:
      return 0
    L = F(node.left)
    R = F(node.right)
    return max(L, R) + 1
  return F(root)

def S(root):
  def F(node, k):
    if node.left:
      F(node.left, k+1)
    if node.right:
      F(node.right, k+1)
    else:
      res.append(k)
      return
  if not root: return 0
  res = []
  F(root, 1)
  return max(res)
