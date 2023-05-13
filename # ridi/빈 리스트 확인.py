# 빈 리스트인지 확인

lst = []
if len(lst) == 0:
  print("비었다.")

lst = []
if not lst:
  print("비었다.")

lst = [1,2,3]
if len(lst) != 0:
  print("안 비었다.")

lst = [1,2,3]
if lst:
  print("안 비었다.")
