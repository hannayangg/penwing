# enumerate 함수 : for 문과 자주 쓰임

# for i, val in enumerate(a): 리스트의 인덱스, 원소

ex = ['원소1', '원소2', '원소3']

for i, val in enumerate(ex):
  print(i, val)

for val in enumerate(ex):
  print(val)