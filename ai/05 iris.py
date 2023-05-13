# [데이터 준비]
# [판다스] iris 데이터 프레임
# [넘파이] iris => xy배열로 변환
import pandas as pd
iris = pd.read_csv(r"C:\Users\ziho1\OneDrive\바탕 화면\vs\ai\Iris.csv")

import numpy as np
xy = np.array(iris)

'''
참고
[오름차순 정렬] np.sort()
[오름차순의 인덱스] np.argsort()
import numpy as np
a = np.array([5,3,4])
print(np.sort(a))
print(np.argsort(a))
'''

# [K_NN]
# 목표: 특성값을 분석해 종류를 알아내기
# 특성: SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm
# 종류: Species
features = xy[:, 1:5]
species = xy[:, -1]

def Distance(A,B):
    return np.sqrt(np.sum((A-B)**2))

def K_NN(Unknown, features, K):

    distance_result = np.zeros(150)
    for i in range(150):
        distance_result[i] = Distance(Unknown, features[i])
    # i 반복문 결과: Unknown과 features[0~149]의 거리들 계산
    # distance_result = [5,2,3,...,1] 150개

    index = distance_result.argsort()
    # Unknown에서 가까운 거리 순 인덱스 저장
    # index = [149,1,2,0,...,0] 150개

    # 결국, index의 상위 k개 중 가장 많이 나온 종류를 찾아내면 됨!
    # k=3 : 상위 3개 중 가장 많이 나온 종류!
    # index[0] = 149 / species[149] = 'virginica'
    # index[1] = 1 / species[1] = 'setosa'
    # index[2] = 2 / species[2] = 'setosa'
    # 결론 setosa

    target_result = []
    result = [0,0,0]

    for i in range(K):
        target_result.append(species[index[i]])
        # target_result = ['virginica', 'setosa', 'setosa']

        if target_result[i] == 'Iris-setosa':
            result[0] += 1
        elif target_result[i] == 'Iris-versicolor':
            result[1] += 1
        else:
            result[2] += 1
        # result = [2,0,1]
    
    max_label = result.index(max(result))
    # max_label = 최댓값 2의 인덱스 = 0

    lables = {0:"setosa", 1:"versicolor", 2:"virginica"}
    species_result = lables[max_label]
    # species_result = lebles[0] = 'setosa'
    
    print(target_result)
    print(result)
    return species_result


# [가상의 데이터 분류하기]
test = np.array([6,2.9,5,2])
print(K_NN(test, features, 5))