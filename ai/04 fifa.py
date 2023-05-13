# [데이터 준비 pandas]
# 1. fifa2019 - 파일 저장
# 2. df - 'Overall'기준 상위 200명 선수 데이터만 저장 (상위: 내림차순)
# 3. test_df - df에서 특정 칼럼만 남겨서 저장

import pandas as pd
fifa2019 = pd.read_csv(r"C:\Users\ziho1\OneDrive\바탕 화면\vs\ai\fifa2019.csv")

df=pd.DataFrame.copy(fifa2019.sort_values(by='Overall', ascending=False).head(200))
a = df.loc[:5, ['Overall']] # 지정 출력 : loc[행 범위, ['열이름']]

a = ['Name', 'Stamina', 'Dribbling', 'ShortPassing', 'Penalties']
test_df = pd.DataFrame(df, columns=a)


# [넘파이 배열]
# 1. test_df -> 배열 XY 변환
# 2. 배열 XY -> 'Stamina, Dribbling'만 들어간 배열 X 변환
# XY는 2차원 배열. 전체 행, 1-2번 열 지정!!

import numpy as np
XY = np.array(test_df)
X = XY[:,1:3]


# [k-means 알고리즘]
# 목표: 200 명의 선수 X => 체력,드리블링 기준 => k개 군집화
# 중심 C 설정
# 중심에서 가까운 데이터들을 모아 평균내어 중심 C 갱신 / 기존 중심은 C_old
# C 와 C_old 차이남
# 다시 중심 C 갱신 / 기존 중심은 C_old
# C 와 C_old 차이 없음
# 완료

def Distance(A,B):
    return np.sqrt(np.sum((A-B)**2))

k = 3
C_x = np.random.choice(X[:,0], k)
C_y = np.random.choice(X[:,1], k)
C = np.array(list(zip(C_x, C_y)))

C_old = np.zeros(C.shape)
flag = Distance(C, C_old)

distance=[]
clusters=np.zeros(len(X))
from copy import deepcopy

while flag !=0:
    for i in range(len(X)): # 0번 선수
        for j in range(k): # 0번 중심
            temp = Distance(X[i], C[j]) # temp = 3
            distance.append(temp) # distance = [3] 추가
            # 다음: 1번 중심, temp = 2, distance = [3,2]
            # 다음: 2번 중심, temp = 5, distance = [3,2,5]
            # i=0, j반복문 결과 distance = [3,2,5] 다 넣었으니 반복문 빠져나와
        
        cluster = np.argmin(distance)
        # cluster = [3,2,5]의 최솟값 인덱스 = 1
        
        clusters[i] = cluster
        # clusters[0] = 1
        # 0번 선수에 1이 할당됨
        
        distance = []
        # 1번 선수 새롭게 distance 구해야 하므로 초기화
        # clusters[1] = 2
        # clusters[2] = 0 ...
        # clusters = np.array([1,2,0,....,2,1,0])

    C_old = deepcopy(C)
    for j in range(k):
        points = [X[i] for i in range(len(X)) if clusters[i] == j]
        C[j] = np.mean(points)
        
        # points = X[0]~X[149] 중에 들어감
        
        # j=0일때
        # clusters[0],clusters[1] == 0 이라고 치면
        # points = [X[0], X[1]]
        # C[0] = points의 평균
        
        # j=1일때
        # clusters[2],clusters[3] == 1이라고 치면
        # points = [X[2], X[3]]
        # C[1] = points의 평균 
        
        # 인덱스가 0인 선수들 => points리스트에 넣고 => 평균을 C[0]로 정의
        # 인덱스가 1인 선수들 => points리스트에 넣음 => 평균을 C[1]로 정의
        # 인덱스가 2인 선수들 => points리스트에 넣음 => 평균을 C[2]로 정의
        
        # points줄 뒤에 바로 C[j]가 있음..
        # j=0인거 points에 넣자마자 바로 C[0] 찾아짐..

    flag = Distance(C,C_old)

print(flag)
print(C)


# [시각화]
'''
참고
X = np.array([[1,2],[3,4],[5,6]])
y = np.array([7,8,9])

print(X[y==7]) => 7에 대응되는 것은 [[1,2]] 2치원임. 이걸 x축y축으로 쪼갬
print(X[y==7,0]) => 그 중 0번은 [1]
print(X[y==7,1]) => 그 중 1번은 [2]
넘파이 배열이 아니라 리스트일 때는 안됨.
'''
# 1. 중심 C
# C = [[65,26,82],[65,26,82]]
# x축: 체력 = 모든 행, 0번 열 (65,26,82)
# y축: 드리블 = 모든 행, 1번 열 (65,26,82)

# 2. 1번 군집 (clusters=0)
# 1번 군집 = [[72,97],[88,88],...] 
# x축: 체력 = clusters=0인 X 중 0번 (72, 88, ...)
# y축: 드리블 = clusters=0인 X 중 1번 (97, 88, ...)


import matplotlib.pyplot as plt
plt.scatter(X[clusters==0,0], X[clusters==0,1])
plt.scatter(X[clusters==1,0],X[clusters==1,1])
plt.scatter(X[clusters==2,0],X[clusters==2,1])
plt.scatter(C[:,0], C[:,1])
plt.show()

