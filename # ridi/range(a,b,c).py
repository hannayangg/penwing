# range(a, b, c)
# a부터 b-1까지 c만큼 건너뛰는 수
#range(0, 50, 5) = 0, 5, 10, 15....45

for i in range(0, 50, 5):
  print(i)

a = [1,2,3,4]
for i in range(len(a)-1, 0, -1): # 3번부터 "1번"(0번 바로전)까지 역순
  print(a[i])

# [4,3,2,1] 로 출력하려면?

for i in range(len(a)-1, -1, -1): # 3번부터 "0번"(-1번 바로전)까지 역순
  print(a[i])