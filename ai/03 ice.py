import csv
import numpy as np

# [데이터 준비 csv]
# 파일 열고 header 처리
f = open(r"C:\Users\ziho1\OneDrive\바탕 화면\vs\ai\temp_ice.csv")
data = csv.reader(f)
header = next(data)
#print(header)

'''
# [데이터 준비 pandas]
df = pd.read_csv(파일경로)
print(df.head(5))
data = np.array(df) - 넘파이 어레이로 저장
X = data[:, 1] - average 온도 어레이
Y = data[:, -1] - ice 판매량 어레이
'''

# [리스트 만들기]
# 평균온도 temp 판매량 ice 에 저장 (avarage는 실수, ice는 정수)
# 기본적으로 엑셀에 저장되어있는 숫자는 "문자열" => int, float써서 수로

temp = []
ice = []
for row in data:
    temp.append(float(row[1])) # for row in data: 데이타의 열 (행이 아님)
    ice.append(int(row[4]))
#print(len(temp), len(ice))
#print(min(temp), max(temp), min(ice), max(ice))


# [온도 구간에 따라 며칠임?]
# 1. 온도 구간 = bins에 저장
# 2. 며칠 = bins에 따른 도수값 출력 np.histogram()
bins = np.arange(min(temp), max(temp)+5, 5)
#print(bins)

hist, bins = np.histogram(temp, bins)
#print(hist)


# [온도 구간에 따라 총 판매량은?]
# 365 중 i번째 온도 (temp[i]) 가
# ex. bins[0] bins[1] 사이라면 ice_buy[0]에 ice[i] 추가
# ex. bins[1] bins[2] 사이라면 ice_buy[1]에 ice[i] 추가
# ex. bins[2] bins[3] 사이라면 ice_buy[2]에 ice[i] 추가
# 즉, bins[j] bins[j+1] 사이라면 ice_buy[j]에 ice[i] 추가

ice_buy = np.zeros(7)

for i in range(len(temp)):
    for j in range(len(bins)): # for 두 줄은 순서 상관x
        if bins[j] <= temp[i] and temp[i] < bins[j+1]:
            ice_buy[j] += ice[i]
#print(ice_buy)


# [온도 구간에 따라 하루 평균 판매량은?]
# ex. -4.1~0.9 도 = 40 일, 총 1106 번 판매 => 하루 평균 = 1106 / 40
# ex. 0.9~5.9 도 = 59일, 총 1659 번 판매 => 하루 평균 = 1659 / 59
# 즉, 판매량을 날짜로 나눠줘야 함 => ice_buy[i] / hist[i]

ice_buy_a = np.zeros(7)
for i in range(len(ice_buy)):
    ice_buy_a[i] = ice_buy[i] // hist[i]
#print(ice_buy_a)


# [선형 회귀 모델 찾기 - 최소제곱법]
# Y = beta1 X + beta0 선형 모델의 beta1,0 찾기
# 1. beta1 = 분자: X오차*Y오차 시그마, 분모: X오차 제곱 시그마
# 2. beta0 = Y평균 - beta1*X평균 (=상수)

X = np.array(temp)
Y = np.array(ice)
mean_x = np.mean(X)
mean_y = np.mean(Y)
n = len(X)

temp1 = 0
temp2 = 0
for i in range(n):
    temp1 += (X[i]-mean_x)*(Y[i]-mean_y)
    temp2 += (X[i]-mean_x)**2
beta1 = temp1 / temp2

beta0 = mean_y - (beta1*mean_x)
print(beta1, beta0)


# [평가 - RMSE함수]
# 분산 : 편차 제곱의 평균
# 표준편차 : 루트 분산
def RMSE(a,b,X,y):
    RMSE = np.sqrt(((y-(a*X+b))**2).mean())
    return RMSE

print(RMSE(beta1, beta0, X,Y))


# [예측함수 만들기]
def Regression(beta0, beta1, X):
    y_pred = beta0 + beta1 * X
    return y_pred

temp = float(input("오늘의 기온: ?"))
result = Regression(beta0, beta1, temp)
print("오늘의 예상 판매량: ", int(result))