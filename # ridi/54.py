# [54 pre, inorder로 이진트리 구축]

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# NEET코드

def F(Pre, In):
  if In:
    root = TreeNode(Pre[0])
    mid = In.index(Pre[0])
    root.left = F(Pre[1:mid+1], In[:mid])
    root.right = F(Pre[mid+1:], In[mid+1:])
    return root



# pop은 한 번 했는데
# left, right에 넘겨지는 Pre리스트가 왜 서로 다르지?

def F(Pre, In):
  if In:
    root = TreeNode(Pre[0])
    mid = In.index(Pre[0])
    Pre.pop(0) ## 이부분이 특이
    
    root.left = F(Pre, In[:mid])
    root.right = F(Pre, In[mid+1:])
    return root
