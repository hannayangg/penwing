# [64. leetcode 572]



def F(root, subRoot):
  def check(n1, n2):
    if not n1 and not n2:
      return True
    if n1 and n2 and n1.val == n2.val:
      return check(n1.left, n2.left) and check(n1.right, n2.right)
    return False
  
  if not root or not subRoot: return False
  if root.val == subRoot.val and check(root, subRoot):
    return True
  return F(root.left, subRoot) or F(root.right, subRoot)