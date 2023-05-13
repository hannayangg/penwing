def recursive_function(num):
    if num < 0:
        print("끝")
    else:
        print(num)
        recursive_function(num-1)
        print('다시 재귀 함수 호출!', num)


recursive_function(5)

# 재귀함수가 스택으로 쌓인다고 생각하면

# Fn(-1) => 종료
# Fn(0) => print 0
# Fn(1) => print 1
# Fn(2)
# Fn(3)
# Fn(4)
# Fn(5)

# 종료조건 바로 상위의 함수부터 프린트 됨


def Fn(lst):
  
  if len(lst) == 0:
    print("끝")
  else:
    print(lst)
    Fn(lst[1:])
    r = lst.pop(0)
    print('!', r)

Fn([1,2,3])