# [59. leetcode 100]



def F(p, q):
  if not p and not q: return True
  elif not p or not q: return False
  elif p.val != q.val: return False
  return F(p.left, q.left) and F(p.right, q.right)