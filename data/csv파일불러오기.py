# [csv 데이터 불러오기 4단계]
# 1. csv 파일을 쉽게 다루도록 도와주는 csv 라이브러리 불러오기
# 2. csv 파일 열기
# 3. 데이터를 컴마로 구분하여 저장하기
# 4. for 반복문으로 한 줄씩 꺼내기

import csv
f = open(  )
data = csv.reader(f)
for row in data:
    print(row)
