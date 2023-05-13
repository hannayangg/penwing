# [60. leetcode 226]



def F(node):
  if not node: return
  node.left, node.right = F(node.right), F(node.left)
  return node
