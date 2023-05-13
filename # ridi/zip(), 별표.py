# zip() 함수

a = [1,2,3,4,5]
b = [2,3,4,5]
c = [3,4,5]

res = zip(a,b) # a의 요소와 b의 요소를 일대일로 묶어서 튜플 형태로 저장
print(res)

res = list(zip(a,b)) # zip의 결과를 추출하기 위해서 list()로 묶어줌
print(res)

res = zip(a,b,c)
print(res)

res = list(zip(a,b,c))
print(res)




# * = unpack

f = ['lemon', 'pear', 'watermelon', 'tomato']
f

# 리스트에서 각 요소만 출력하는 방법
# 1)
print(f[0], f[1], f[2], f[3])

# 2)
for x in f:
  print(x, end=' ')

# 3) * = unpack! f라는 리스트를 풀어헤친다.
print(*f)