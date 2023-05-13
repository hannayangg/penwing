###

h = {'J': ['K', 'N'], 'N': ['J']}
#h['K'] # 오류

import collections
h = collections.defaultdict(list)
tickets=[["J","K"],["J","N"],["N","J"]]
for x in tickets:
  v0, v1 = x
  h[v0].append(v1)
print(h)
h['K']