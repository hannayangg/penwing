# [51 더 큰 수 합계 트리로]

# 내가 푼 것 (반복, st, RNL)
# R 팝된 노드가 R자식 있다면 st에 쌓기.
# N 팝된 노드에 plus값 누적.
# L 팝된 노드가 L자식 있는 경우, st에 쌓기.

def F(root):
  st = [root]
  plus = 0
  seen = set()
  while st:
    node = st.pop()
    if node.right and node.right not in seen:
      st.append(node)
      st.append(node.right)
      seen.add(node.right)
      continue
    node.val += plus
    plus = node.val
    if node.left:
      st.append(node.left)
  return root


# 책 풀이 (재귀, RNL)
# 누적의 순서가 RNL임을 파악하고, RNL재귀함수를 이용.

class Solution:
  plus: int = 0
  def F(self, root):
    if not root:
      return

    self.F(root.right)

    root.val += self.plus
    self.plus = root.val

    self.F(root.left)
    return root