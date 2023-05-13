# [34. leetcode 57]


def F(arr, new):
  res = []
  for i in range(len(arr)):
    l, r = arr[i]

    # new범위에 포함안되는 경우
    if r < new[0] or new[1] < l:
      res.append(arr[i])
      continue
    
    # new 업데이트
    new[0] = min(new[0], l)
    new[1] = max(new[1], r)

  res.append(new)
  return sorted(res)