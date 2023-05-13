# [소인수분해, 최대공약수, 최소공배수]

def SO(x): # 소인수분해
    x = int(x)
    d = 2
    list = []
    while d <= x:
        if x % d == 0:
            list.append(d)
            x = x / d
        else:
            d = d + 1
    return list
    
# [x=15] [d=2]
# 15%2 != 0 -> d=3
# 15%3 == 0 -> list=[3] x=5
# 5%3 != 0 -> d=4
# 5%4 != 0 -> d=5
# 5%5 == 0 -> list=[3,5] x=1
# d=5, x=1 이므로 종료

def 최대공약수(a,b):
    a = SO(a)
    b = SO(b)
    if len(a) < len(b):
      n = len(a)
    else:
      n = len(b)
    list = 1
    for i in range(len(a)):
        if a[i] in b:
            list *= a[i]
            b.remove(a[i])
    return list

# a[0] in b: list.append(a[0]) b.remove(a[0]) --> b에서 카운트 된 원소는 빼줘야 함
# a[1] in b: list.append(a[1]) b.remove(a[1])
# a[2] in b: list.append(a[2])

def 최소공배수(a,b):
    temp = 최대공약수(a,b)
    A = a / temp
    B = b / temp
    return temp * A * B


'''
def 곱(x): # 리스트 원소들의 곱
  a = 1
  for i in range(len(x)):
    a *= x[i]
  return a


최대공약수 다른 방법
1. if문 두개

a = [1,2,3]
b = [1,2,4]
lst = []
for i in range(len(a)):
  if a[i] in b:
    if a[i] not in lst
      lst.append(a[i])
print(lst)

2. 집합 이용

a = [1,2,3]
b = [1,2,4]
result = set()
for i in range(len(a)):
  if a[i] in b:
    result.add(a[i])
print(result)

이후에 다시 리스트로 바꿀 수 있음!!!
lst = list(result)
print(lst)
'''