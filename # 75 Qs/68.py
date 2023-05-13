# [68. leetcode 235]




# 루트부터 전체순회.
# p, q의 부모들을 리스트에 각각 담기.

def S(root, p, q):
  p_root = []
  q_root = []
  
  def F(node, tmp):
    nonlocal p_root
    nonlocal q_root
    if not node: return
    if node == p: p_root = tmp + [node]
    if node == q: q_root = tmp + [node]
    F(node.left, tmp + [node])
    F(node.right, tmp + [node])
  
  F(root, [])
  res = root
  while p_root and q_root and p_root[0] == q_root[0]:
    res = p_root.pop(0)
    q_root.pop(0)
  return res



# BST를 이용하기. (p,q.val 와 root.val 비교)

def F(root, p, q):
  if root.val < p.val and root.val < q.val:
    return F(root.right, p, q)
  elif root.val > p.val and root.val > q.val:
    return F(root.left, p, q)
  else:
    return root