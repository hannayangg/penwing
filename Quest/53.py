# [53. leetcode 20]



def F(s):
  hash = {"(": ")", "[": "]", "{": "}"}
  st = []
  for char in s:
    if char in hash:
      st.append(char)
      continue
    if not st or char != hash[st.pop()]:
      return False
  return not st