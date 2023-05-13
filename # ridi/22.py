# [22 일일온도]


# 내가 푼 것
# 스택에 인덱스와 값 저장
# 스택의 탑보다 큰 값이 등장할 경우, 인덱스의 차이 저장

def F(T):
  S = [0] * len(T)
  st = []
  for i, v in enumerate(T):
    while st and v > st[-1][1]: # 스택의 탑보다 클 경우
      p = st.pop()
      S[p[0]] = i-p[0]
    st.append((i, v))
  return S


# 책 풀이
# 스택에 인덱스만 저장
# 대신, 값 비교 할 때마다 T[idx]로 비교.

def F(T):
  S = [0] * len(T)
  st = []
  for i, v in enumerate(T):
    while st and v > T[st[-1]]: ###
      p = st.pop()
      S[p] = i-p
    st.append(i)
  return S