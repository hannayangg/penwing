# [61. leetcode 124]




def F(root):
  path = root.val
  
  def dfs(node):
    nonlocal path
    if not node: return 0
    
    # LR음수일 땐 0처리.
    L = max(0, dfs(node.left))
    R = max(0, dfs(node.right))

    # path값 업데이트.
    path.append(L+R+node.val)
    
    return max(L, R) + node.val
  
  dfs(root)
  return path