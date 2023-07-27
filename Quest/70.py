# [70. leetcode 211]


class TrieNode:
  def __init__(self):
    self.children = {}
    self.isEnd = False

class WordDictionary:
  def __init__(self):
    self.root = TrieNode()
  def addWord(self, word):
    cur = self.root
    for c in word:
      if c not in cur.children:
        cur.children[c] = TrieNode()
      cur = cur.children[c]
    cur.isEnd = True
  
  def search(self, word):
    def dfs(i, cur):
      
      # 종료조건
      if i >= len(word): return cur.isEnd 

      # '.'일 때
      if word[i] == '.':
        for child in cur.children.values():# node.children = 해쉬맵 자체.
          if dfs(i+1, child):
            return True
        return False
      
      # False
      elif word[i] not in cur.children:
          return False
      
      # True
      return dfs(i+1, cur.children[word[i]])
      
    return dfs(0, self.root)   
