# [12 주식을 사고팔기 가장 좋은 시점]

# 내가 푼 것

def F(stock):
  profit = 0
  mini = float("inf")
  for i, v in enumerate(stock):
    profit = max(profit, v-mini)
    if v < mini:
      mini = v
  return profit


# 책 풀이: for 문 돌면서 해당 위치에서의 최솟값, 이익을 갱심
# 최솟값 찾을 때 min(mini, v) 활용
# 시스템에서 지정하는 최댓값 sys.maxsize이 float("inf")보다 빠른듯.

import sys

def F(stock):
  profit = 0 # 최솟값으로 시작 => 갱신될 수 있도록
  mini = sys.maxsize # 최댓값으로 시작 => 갱신될 수 있도록

  for x in stock:
    profit = max(profit, x-mini)
    mini = min(mini, x)

  return profit