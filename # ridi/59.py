# [59 구간 병합]

# 내가 푼 것
# 스택[-1]과 해당 원소를 비교하며 스택에 담기.

def F(arr):
  arr.sort()
  st = []
  for L, R in arr:
    if st and st[-1][1] >= L:
      st[-1][1] = max(st[-1][1], R)
    else:
      st.append([L, R])
      # st += [L,R],
  return st


# 개선
# st 에 어펜드하는 것 대신 콤마 이용.
# st += i, => 대괄호.