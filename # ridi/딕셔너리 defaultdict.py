# 선언
dic = {}

# 값 지정
dic['a'] = 100
dic['c'] = 10
dic['b'] = 50

# 값 얻기 (두가지)
dic.get('a')
dic['a']

# 값 삭제
#del dic['a']

# 키만 얻기
dic.keys()

# 값만 얻기
dic.values()

# 키, 값 얻기
dic.items()

# 정렬
sorted(dic.items()) # 키로 정렬 -> a,b,c순서
sorted(dic.items(), key = lambda x: x[1]) # 값으로 정렬 -> 10,50,100순서

# 딕셔너리 초기화 : 숫자, 리스트, 세트 가능함

from collections import defaultdict

dic_int = defaultdict(int)
dic_list = defaultdict(list)
dic_set = defaultdict(set)

print(dic_int, dic_int['key'])
print(dic_list, dic_list['key'])
print(dic_set, dic_set['key'])


dic_int['key2'] = '명시적인 값 지정하면 변경됨'
dic_list['key2'] = '명시적인 값 지정하면 변경됨'
dic_set['key2'] = '명시적인 값 지정하면 변경됨'

print(dic_int)
print(dic_list)
print(dic_set)

# defaultdict : 밸류에 삽입하는 게 간단함

name_list = [('kim', 'minkyung'), ('park', 'hyunjeong'), ('kim', 'yura')]
dic_name = defaultdict(list)

for k, v in name_list:
  dic_name[k].append(v) # defaultdict()의 인자로 set 사용시 append() 대신 add() 사용

print(dic_name)

# 원래 내가 알던 방법 : 키가 딕셔너리에 있는지 확인하는 if문 돌리면서 함
name_list = [('kim', 'minkyung'), ('park', 'hyunjeong'), ('kim', 'yura')]
dic_name = dict()

for k, v in name_list:
  if k not in dic_name:
    dic_name[k] = [v]
  else:
    dic_name[k].append(v)

print(dic_name)