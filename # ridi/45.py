# [45 이진 트리 반전]

# 내가 푼 것

def S(root):
  def F(node):
    if not node:
      return
    node.left, node.right = node.right, node.left
    F(node.left)
    F(node.right)
  F(root)
  return root


# 책풀이
# 재귀: root 자신을 리턴, 왼오 자식 스왑도 리턴 값으로 함!

def F(root):
  if root:
    root.left, root.right = F(root.right), F(root.left)
    return root
  else:
    return None