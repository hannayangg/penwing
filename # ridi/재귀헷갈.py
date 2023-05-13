# 재귀 두번 돌릴 때 주의.
# pop한 후 넘겨지는 1) 2) 에서의 arr이 다르다.
# "arr팝되는게 공유됨." -> 개별적으로 하고 싶으면 복사해야 함.

def F(arr):
  print(arr, end=' ')
  if len(arr)==1: return
  arr.pop()
  F(arr) # 1)
  F(arr) # 2)

print(F([1,2,3]))


def F(arr):
  print(arr, end=' ')
  if len(arr)==1: return
  arr.pop()
  arr2 = arr[:]
  F(arr) # 1)
  F(arr2) # 2)

print(F([1,2,3]))