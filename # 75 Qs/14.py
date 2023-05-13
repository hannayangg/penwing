# [14. leetcode 190]


def F(n):
  n = bin(n)
  n = ''.join(list(reversed(n))[:-2])
  plus = '0'*(32-len(n))
  n += plus
  return int(n, 2)