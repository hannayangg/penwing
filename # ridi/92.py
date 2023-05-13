# [b2 다트 게임]

def result(score):
  idx = 0
  st = []
  res = []
  while idx < len(score):
    if score[idx] == 'S':
      res.append(st[-1])
    elif score[idx] == 'D':
      res.append(st[-1]**2)
    elif score[idx] == 'T':
      res.append(st[-1]**3)
    elif score[idx] == '*':
      res[-1] = res[-1]*2
      if len(res) >= 2:
        res[-2] = res[-2]*2
    elif score[idx] == '#':
      res[-1] = -res[-1]
    else:
      if score[idx] == '0' and st[-1] == 1:
        st[-1] = 10
      else:
        st.append(int(score[idx]))
    idx += 1
  return sum(res)