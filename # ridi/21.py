# [21. 중복 문자 제거]


# 분리 & 재귀
# 필요한 문자가 다 있는 구간을 찾아 분리하여, 재귀에 넣기.

def F(s):
  for char in sorted(set(s)):
    prefix = s[s.index(char):]

    if set(prefix) == set(s):
      return char + F(prefix.replace(char, ''))

  return ''



# F(cbacdcbc) = a + F(cdcbc)
# F(cdcbc) = c + F(db)
# F(db) = d + F(b)
# F(b) = b + F()