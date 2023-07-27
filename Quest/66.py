# [66. leetcode 980]



import sys

# 재귀함수 F(node, left, right) 호출 시 left, right의 범위를 변경. 



def F(root):

  def valid(node, left, right):
    # True 조건
    if not node: return True
    # False 조건
    if not (left < node.val < right): return False
    # recursive call
    return valid(node.left, left, node.val) and valid(node.right, node.val, right)
  
  return valid(root, -sys.maxsize, sys.maxsize)