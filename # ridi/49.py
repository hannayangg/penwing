# [49 최소 높이 트리]

# 가장 가운데에 있는 값이 루트.
# 리프 노드를 하나씩 제거하고 남은 값이 가운데.

n = 6
edges = [[0,3],[1,3],[2,3],[4,3],[5,4]]

import collections
gragh = collections.defaultdict(list)
for i, j in edges:
  gragh[i].append(j)
  gragh[j].append(i)
print(gragh)

# 리프노드들만 leaves에 추가
leaves = []
for i in range(n+1):
  if len(gragh[i]) == 1:
    leaves.append(i)
print(leaves)

# 가운데 값이 2개 이하일 때까지 리프노드 계속 제거
while n > 2:
  n -= len(leaves)
  new_leaves = []
  for leaf in leaves:
    neighbor = gragh[leaf].pop()
    gragh[neighbor].remove(leaf)

    if len(gragh[neighbor]) == 1:
      new_leaves.append(neighbor)
  leaves = new_leaves
