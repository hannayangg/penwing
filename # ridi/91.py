# [b1 비밀 지도]

import re
def secret(n, arr1, arr2):
  res = []
  for i in range(n):
    x = bin(arr1[i] | arr2[i])[2:]
    x = re.sub(r'[1]', '#', x)
    x = re.sub(r'[0]', ' ', x)
    res.append(x)
  return res

  
secret(5, [9,20,28,18,11], [30,1,21,17,28])
secret(6, [46,33,33,22,31,50],[27,56,19,14,14,10])