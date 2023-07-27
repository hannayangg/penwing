# [67. leetcode 230]

# LNR 순서로 리스트에 담기기
def S(root, k):
  st = []
  def F(node):
    if not node: return
    F(node.left)
    st.append(node.val)
    F(node.right)
  return st[k-1]