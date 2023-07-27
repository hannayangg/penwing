# [69. leetcode 208]


# 트라이노드부터 설정.
# TrieNode구조: children{} 가지고, isEnd = False.


class TrieNode:
  def __init__(self):
    self.children = {}
    self.isEnd = False
class Trie:
  def __init__(self):
    self.root = TrieNode()
  def insert(self, word):
    cur = self.root
    for c in word:
      if c not in cur.children:
        cur.children[c] = TrieNode()
      cur = cur.children[c]
    cur.isEnd = True