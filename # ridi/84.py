# [84 괄호 삽입]


# "-+*" 앞 뒤로 L, R 분할.
# L에서 받은 리스트와 R에서 받은 리스트를 연산. 결과들 리스트로 리턴.


def compute(L, R, op):
  res = []
  for l in L:
    for r in R:
      res.append(eval( str(l)+op+str(r)) )
  return res

def F(input):
  # 숫자밖에 없는 경우 바로 리턴 ("2" -> [2])
  if input.isdigit(): return [int(input)]
  
  res = []
  for i, v in enumerate(input):
    if v in "+-*":
      L = F(input[:i])
      R = F(input[i+1:])
      res.extend(compute(L, R, v))
  return res


# append() vs extend()
# 리스트를 풀어서 각각원소로 확장해 삽입