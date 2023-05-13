# [44 가장 긴 동일값의 경로]

# 내가 푼 것
# F(node) -> 바로 node.left, node.right도 함수 돌려야 함 (건너뛰지 않도록)

def S(root):
  if not root: return 0
  result = []
  def F(node):
    if not node: return 0
    L = F(node.left)
    R = F(node.right)

    if node.left and node.val != node.left.val:
      L = 0
    if node.right and node.val != node.right.val:
      R = 0
    result.append(L+R)
    return max(L, R) + 1
  F(root)
  return max(result)
