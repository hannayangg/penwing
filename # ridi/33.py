# [33 전화번호 문자조합]

# 내가 푼 것

def F(digits):
  def dfs(idx, letter):
    if idx == len(digits):
      result.append(letter)
      return
    for x in dic[digits[idx]]: ##
      dfs(idx+1, letter+x)

  if not digits: return []
  dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
       '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
  result = []
  dfs(0, '')
  return result

# 책 풀이 (## 부분이 추가됨)
# for i in range(idx, len(digits)) 반복문이 늘어났는데 왜 더 빠르지?