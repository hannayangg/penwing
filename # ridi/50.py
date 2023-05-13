# [50 정렬된 배열 - 이진 탐색 트리 변환]
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# 내가 푼 것
# 재귀: 리스트 중간을 루트로 만들고, LR자식 재귀호출 리턴값으로 연결

def F(nums):
  if not nums:
    return None
  m = len(nums) // 2
  root = TreeNode(nums[m])
  root.left = F(nums[:m])
  root.right = F(nums[m+1:])
  return root