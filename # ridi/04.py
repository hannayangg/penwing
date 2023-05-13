# [04 흔한 단어 찾기]

import re, collections

# 내가 푼 것

def F(paragragh, banned):
  para = re.sub('[^a-z0-9]', ' ', paragragh.lower()).split()
  hash = collections.Counter(para)
  for char in banned:
    if char in hash: hash.pop(char)
  return hash.most_common(1)[0][0]


# 개선 - 애초에 딕셔너리에 담을 때, banned 에 없는 것만 담는다.
# 특수문자 제거 - re.sub(r'[^\w]', ' ', text)

def common(paragraph, banned):
  para = re.sub(r'[^\w]', ' ', paragraph).lower().split()
  words = [word for word in para if word not in banned]
  hash = collections.Counter(words)
  return hash.most_common(1)[0][0]