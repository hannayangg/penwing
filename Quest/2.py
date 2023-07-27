# [2. leetcode 121]



# 내가 푼 것 - 최대, 최소 매번 업데이트하기.
import sys
def F(prices):
    min = sys.maxsize
    profit = 0
    for i, v in enumerate(prices):
        if v < min: min = v
        profit = max(profit, v-min)
    return profit


# 투포인터.

def F(input):
  l, r = 0, 1
  res = 0
  while r < len(input):
    if input[l] < input[r]:
      res = max(res, input[r]-input[l])
    else:
      l = r # l보다작은 r => buy지점!!
    r += 1
  return res