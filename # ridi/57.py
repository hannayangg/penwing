# [57 팰린드롬 페어]

# 방법1) 시간초과

from itertools import permutations
word = ['abcd', 'dcba', 'lls', 's', 'sssll']

# 팰린드롬인지 확인
def Fn(a):
  return a == a[::-1]

# 가능한 조합
res = []
w = list(permutations(word,2))
for v0, v1 in w:
  if Fn(v0+v1):
    x = word.index(v0)
    y = word.index(v1)
    res.append([x,y])
print(res)

# 가능한 조합을 찾는 다른 방법
res = []
for i, word1 in enumerate(word):
  for j, word2 in enumerate(word):
    if i == j:
      continue
    if Fn(word1 + word2):
      res.append([i, j])
print(res)