# [72. leetcode 347]


# 리스트 이용하는 방법: 인덱스 = 등장횟수, 값 = 해당숫자 저장.

def F(nums, k):
  h = {}
  freq = [[] for i in range(len(nums)+1)]

  for n in nums:
    h[n] = 1 + h.get(n, 0)

  for n, c in h.items():
    freq[c].append(n)

  res = []
  for i in range(len(freq)-1, 0, -1):
    for n in freq[i]:
      res.append(n)
      if len(res)==k:
        return res