# [03 로그 파일 재정렬]

# 내가 푼 것
# 정렬 기준 두 개: lambda x:(기준1, 기준2
# 알파벳인지 확인: .isalpha()

def F(logs):
  lt = []
  dg = []
  for l in logs:
    if l[-1].isalpha(): lt.append(l)
    else: dg.append(l)

  lt.sort(key = lambda x: (x.split()[1:], x.split()[0]))
  return lt + dg