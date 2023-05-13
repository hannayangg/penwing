# [46 두 이진 트리 병합]

# 내가 푼 것
def F(root1, root2):
  if not root1 and root2: # 개선 -> 걍 return root1 or root2
    return root2
  if root1 and root2:
    root1.val += root2.val
    root1.left, root1.right = F(root1.left, root2.left), F(root1.right, root2.right)
  return root1


# 책 풀이 - 아예 새로운 트리노드를 만듦.
class TreeNode:
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None

def F(root1, root2):
  if root1 and root2:
    node = TreeNode(root1.val + root2.val)
    node.left = F(root1.left, root2.left)
    node.right = F(root1.right, root2.right)
    return node
  else:
    return root1 or root2