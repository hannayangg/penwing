# [52 이진탐색트리 합의 범위]

# 내가 푼 것

class Solution:
  res: int = 0
  def F(self, root, L, R):
    if not root:
      return
    self.F(root.left, L, R)
    self.res += root.val if L <= root.val <= R else 0
    self.F(root.right, L, R)
    return self.res

# 책 풀이
# res 저장공간 없이 풀이
# 리턴 = 루트값 + LR자식들 리턴값

def F(root, L, R):
  if not root: 0
  return (root.val if L <= root.val <= R else 0) + F(root.left, L, R) + F(root.right, L, R)


# 가지치기
# L보다도 작은 root => R자식만 호출
# R보다도 큰 root => L자식만 호출

def F(root, L, R):
  if not root:
    return 0
  if root.val < L:
    return F(root.right, L, R)
  elif root.val > R:
    return F(root.left, L, R)
  else:
    return root.val + F(root.left, L, R) + F(root.right, L, R)