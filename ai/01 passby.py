# [리스트]
# 1차원 리스트
a = [10,20,30]
b = []
c = list(range(1,10))
print(a,b,c)

# [리스트의 함수]
# len(리스트명) : 리스트에 저장된 데이터의 개수
# 리스트명.append(데이터) : 리스트의 마지막에 데이터 추가
# 리스트명.insert(인덱스, 데이터) : 리스트의 원하는 인덱스에 데이터 삽입
# 리스트명.remove(데이터) : 리스트에서 첫번째로 나오는 해당 데이터 삭제
# 리스트명.sort() : 리스트의 데이터 오름차순 정렬
# 내림차순 함수는 없음 -> 오름차순 정렬 후 역순으로 배열
# 리스트명.reverse() : 리스트의 데이터 역순으로 배열
a = [5,10,3,40]
print(len(a))
a.append(50)
print(a)
a.insert(2,7)
print(a)
a.remove(50)
print(a)
a.sort()
print(a)
a.reverse()
print(a)

# [데이터 준비]
# 1. 파일을 딕셔너리 형태로 읽기 : csv.DictReader(파일객체명)
# 2. 저장할 2차원 배열 a 만들기 : 2차원 배열 내 각 요일이 1차원으로 들어감
# 3. i요일, j시간대 초기화
# 4. reader 의 행(=j시간대) 을 a[i](=i요일) 에 추가
# - j=j+1 시간대를 하나씩 올리며 24시간대까지 a[i]에 추가함
# - 언제까지? j가 24를 넘어가면 다음 요일이기 때문에 i를 1 늘려야 함
# - 어떻게 식으로 쓰지? j=0,1,2,3,,,23 까지는 괜찮음, j=24부터 다음요일
# - j=0,1,2,3,,,23 과 j=24 를 구분하려면 : j%24==0
#   (j%24 !=0)      (j%24==0)

import csv
a = [[],[],[],[],[],[],[]]
with open('C:\\Users\\ziho1\\OneDrive\\바탕 화면\\vs\\ai\\passby.csv','r') as file:
    reader = csv.DictReader(file)
    i = j = 0
    for row in reader:
        a[i].append(row)
        j = j+1
        if(j%24==0):
            i = i+1
for i in range(7):
    for j in range(24):
        print([i], a[i][j]) # 요일, 요일의 각 시간대
# [시간대 별 행인수 평균]

# 0시일 때 월~일 인구수의 평균값 구하기
# 1. j=0 일때 i=0~6 인구수를 누적하여 sum에 저장
# 2. sum을 7로 나눈 평균값을 avgh 리스트에 넣음 (0번 인덱스)
# 3. sum 초기화 => j=1일 때 sum을 새로 구해야 하기 때문

# 1시일 때 월~일 인구수의 평균값 구하기
# 1. j=1 일때 i=0~6 인구수를 누적하여 sum에 저장
# 2. sum을 7로 나눈 평균값을 avgh 리스트에 넣음 (1번 인덱스)
# 3. sum 초기화

# 이를 24번 반복

avgh=[]
for j in range(24):
  sum=0
  for i in range(7):
    sum += int(a[i][j]['num'])
  avgh.append(sum / 7)
print(avgh)

# avgh를 소수점 없이 정수로만 출력하기

for i in range(24):
  print(int(avgh[i]))

# [시간대 별 행인수, 여성행인수, 30대이하 행인수 평균 구하기]
# 응용

avgh=[]
avgh_w=[]
avgh_y=[]
for j in range(24):
  sum=0
  sum_w=0
  sum_y=0
  for i in range(7):
    sum += int(a[i][j]['num'])
    sum_w += int(a[i][j]['wnum'])
    sum_y += int(a[i][j]['ynum'])    
  avgh.append(sum // 7)
  avgh_w.append(sum_w // 7)
  avgh_y.append(sum_y // 7)

print(avgh)
print(avgh_w)
print(avgh_y)

# [꺾은선그래프 시각화]
# 시간대 별 행인수, 여성행인수, 30대이하 행인수 평균
# x축 : 시간대, y축 : 평균들
# x축 정의해야 함
# y축이 1차원 => x축도 1차원 리스트

import matplotlib.pyplot as plt

x = list(range(24))

plt.plot(x, avgh, label='avgh', c='blue')
plt.plot(x, avgh_w, label='avgh_w', c='red')
plt.plot(x, avgh_y, label='avgh_y', c='green')
plt.legend()
plt.show()