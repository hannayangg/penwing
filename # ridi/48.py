# [48 균형 이진 트리]

# 내가 푼 것
def S(root):
  def F(node):
    if not node:
      return 0
    L = F(node.left)
    R = F(node.right)
    res.append(abs(L-R))
    return max(L, R) + 1
  res = []
  F(root)
  return not res or max(res) <= 1 # []도 True 리턴



# 책 풀이 (res 저장공간x)
# 리턴 값 = 최대높이 or -1 (여기서 -1은 False 의미)

def S(root):
  def F(node):
    if not node:
      return 0
    L = F(node.left)
    R = F(node.right)
    if L == -1 or R == -1 or abs(L-R) > 1:
      return -1
    return max(L, R) + 1
  return F(root) != -1