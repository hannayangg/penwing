# [43 이진 트리의 최대 직경]

# 내가 푼 것
def S(root):
  res = 0
  def F(node):
    nonlocal res
    if not node: return 0
    L = F(node.left)
    R = F(node.right)
    res = max(res, L + R)
    return max(L, R) + 1
  F(root)
  return res


# 책 풀이: 변수 설정.
# class Solution:
#   result: int = 0
# 이제 내부 함수에서 self.result 변수를 사용할 수 있음.