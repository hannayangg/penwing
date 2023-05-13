# [65. leetcode 105]


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Pre: 루트노드.
# In: 루트인덱스 기준으로 좌우가 자식노드.

def F(Pre, In):
  if not Pre or not In: return None
  val = Pre.pop(0)
  root = TreeNode(val)
  if not Pre: return root
  i = In.index(val)
  root.left = F(Pre, In[:i])
  root.right = F(Pre, In[i+1:])
  return root



# Pre.pop(0) 대신 Pre의 인덱스를 조정하는 방법.

def F(Pre, In):
  if not Pre or not In: return None
  root = TreeNode(Pre[0])
  i = In.index(Pre[0])
  root.left = F(Pre[1:i+1], In[:i])
  root.right = F(Pre[i+1:], In[i+1:])
  return root