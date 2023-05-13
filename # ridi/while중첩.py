# while문이 중첩된 경우
# 안 while 종료 => 바깥 while

a = 1
while a < 3:
  b = 1
  while b < 3:
    print(a, b, a*b)
    b += 1
  a += 1