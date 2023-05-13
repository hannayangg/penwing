# [72 두 정수의 합]

# 내가 푼 것
def S(a, b):
  return sum([a, b])


# 니트코드 풀이 (두 수 부호 다를 땐 오류)

a, b = 2, 3
while b!=0:
  a, b = (a^b), ((a&b)<<1)
print(a)


# 책 풀이 (비트마스크, 최대정수비트 가 이해가 안됨)

a, b = 2, -4
# 비트마스크 (2의 보수로 만듦)
MASK = 0xFFFFFFFF
# 최대 정수비트 (2147483647)
INT_MAX = 0x7FFFFFFF

while b!=0:
  a, b = (a^b)&MASK, ((a&b)<<1)&MASK

if a > INT_MAX:
  a = ~(a^MASK)
print(a)
