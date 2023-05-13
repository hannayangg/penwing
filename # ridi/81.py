# [81 주유소]

# 내가 푼 것
# 양수 나오면 시작점 기록. 이후 값 next에 누적. next < 0 -> 시작점 업데이트.

def F(gas, cost):
  if sum(gas) < sum(cost):
    return -1
  next = None
  prev = 0
  for i in range(len(gas)):
    node = gas[i] - cost[i]
    if next is None:
      if node < 0:
        prev += node
      else:
        start = i
        next = node
    else:
      if next >= 0:
        next += node
      else:
        start = i
        prev += next
        next = node
  return start



# 니트코드
# fuel 누적값 음수 = 출발불가지역. => start 업데이트 & fuel을 초기화.
# (start에서 새로 시작해 뒤로 누적)

def F(gas, cost):
  if sum(gas) < sum(cost):
    return -1
  fuel = 0
  start = 0
  for i in range(len(gas)):
    fuel += gas[i] - cost[i]
    # 출발불가지역 판별 / start업데이트
    if fuel < 0:
      start = i+1
      fuel = 0
  return start