# [56 트라이 구현]

# 니트코드 - 반복, 간결
# word를 순회해 자식노드 만들며 연결.
# (루트에서 시작한 노드를 업데이트하기.)

class TrieNode:
  def __init__(self):
    self.children = {}
    self.endOfWord = False

class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word):
    cur = self.root
    for c in word:
      if c not in cur.children:
        cur.children[c] = TrieNode()
      cur = cur.children[c]
    cur.endOfWord = True
  
  def search(self, word):
    cur = self.root
    for c in word:
      if c not in cur.children:
        return False
      cur = cur.children[c]
    return cur.endOfWord

  def startsWith(self, word):
    cur = self.root
    for c in word:
      if c not in cur.children:
        return False
      cur = cur.children[c]
    return True



# 코없 참고한 것 - 재귀, 좀더 복잡.
# 책 풀이 - 반복, 콜렉션의 디폴트딕을 사용하여 좀더 간결. 