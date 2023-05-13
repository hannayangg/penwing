# [47 이진 트리 직렬화 역직렬화]

import collections
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Codec:
  def serialize(self, root):
    res = ['#']
    q = [root]
    while q:
      node = q.pop(0)
      if node:
        q.append(node.left)
        q.append(node.right)
        res.append(str(node.val))
      else:
        res.append('#')
    return ' '.join(res)

  def deserialize(self, data):
    if data == '# #': # 데이터 빈 경우
      return None
    nodes = data.split()
    root = TreeNode(int(nodes[1])) # (int 안해도 됨. 문자열 '2'도 노드 만들어짐)
    q = [root]
    idx = 2
    while q:
      node = q.pop(0)
      if nodes[idx] is not '#':
        node.left = TreeNode(int(nodes[idx]))
        q.append(node.left)
      idx += 1
      if nodes[idx] is not '#':
        node.right = TreeNode(int(nodes[idx]))
        q.append(node.right)
      idx += 1
    return root







