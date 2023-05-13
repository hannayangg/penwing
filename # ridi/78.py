# [78 주식 사고 팔기]


# 내가 푼 것
def F(prices):
  minp = prices[0]
  res = 0
  for i,v in enumerate(prices):
    if i == 0: continue
    if minp < v:
      res += (v-minp)
    minp = v
  return res

# 니트코드 / 책
def F(prices):
  res = 0
  for i in range(1, len(prices)):
    if prices[i-1] < prices[i]:
      res += prices[i] - prices[i-1]
  return res