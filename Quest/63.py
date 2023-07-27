# [63. leetcode 297]

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Pre-order 방법으로 풀어보기.

def serialize(root):
  res = []
  def dfs(node):
    if not node:
      res.append('N')
      return
    res.append(str(node.val))
    dfs(node.left)
    dfs(node.right)
  dfs(root)
  return ','.join(res)



# deserialize : 부모노드 만든 후, 자식노드 dfs로 연결.

def deserialize(s):
  s = s.split(',')
  i = 0
  def dfs():
    nonlocal i
    if s[i] == 'N':
      i += 1
      return None
    node = TreeNode(int(s[i]))
    i += 1
    node.left = dfs()
    node.right = dfs()
    return node
  return dfs()







# 내가 푼 것 : q 이용.

def serialize(root):
  if not root: return ''
  res = ''
  q = [root]
  while q:
    node = q.pop(0)
    if not node:
      res += 'N,'
      continue
    res += str(node.val) + ','
    q.append(node.left)
    q.append(node.right)
  return res


def deserialize(s):
  if not s: return None
  s = s.split(',')
  root = TreeNode(s[0])
  q = [root]
  i = 1
  while q:
    node = q.pop(0)
    if i < len(s) and s[i] != 'N':
      node.left = TreeNode(s[i])
      q.append(node.left)
    i += 1
    if i < len(s) and s[i] != 'N':
      node.right = TreeNode(s[i])
      q.append(node.right)
    i += 1    
  return root


