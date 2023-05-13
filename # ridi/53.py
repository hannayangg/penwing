# [53 이진탐색트리 노드간 최소 거리]

# 내가 푼 것
# 재귀, RNL: 이전, 현재 노드의 차이값을 업데이트

import sys
def S(root):
  diff = last = sys.maxsize
  
  def F(root):
    nonlocal last
    nonlocal diff
    if not root: return
    F(root.right)

    diff = min(diff, last - root.val)
    last = root.val
    
    F(root.left)
  F(root)
  return diff