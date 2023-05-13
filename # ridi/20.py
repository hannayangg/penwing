# [20 유효한 괄호]

# 스택의 세 가지 명령어
# push : 제일 위에 추가 [append()]    
# pop  : 제일 위의 것을 삭제 [pop()]
# top  : 제일 위의 것에 접근하기 [lst[-1]]

# 내가 푼 것 - 딕셔너리에 저장
def F(s):
  h = {')': '(', ']': '[', '}': '{'}
  st = []
  for c in s:
    if c == '(' or c == '[' or c == '{':
      st.append(c)
    elif st and st[-1] == h[c]:
      st.pop()
    else:
      return False
  return not st


# 개선
# if 문 대신 : 매핑테이블에 없으면 푸시 (,[,{ 이것들
# st[-1] 비교 대신 : 무조건 팝한 후 비교

def F(s):
  h = {')': '(', ']': '[', '}': '{'}
  st = []
  for c in s:
    if c not in h:
      st.append(c)
    elif not st or st.pop() != h[c]:
      return False
  return not st