# 적경을 각도로 변환(시:분:초)

def hms2dec(h, m, s):
  return 15 * (h + m/60 + s/(60*60))


# 적위를 각도로 변환(각:arcmin:arcsecond)

def dms2dec(d, m, s):
  if d >= 0:
    return d + m/60 + s/(60*60)
  return -1 * (-d + m/60 + s/(60*60))



# 각거리 공식
# (r1, d1) ~ (r2,d2) 사이 각거리.
# 여기서 r1, d1는 모두 좌표로, 각도임. (위에서 변환한 각도)
# degrees를 받아서 radian으로 바꾸어 계산, 각거리 결과는 다시 degree로.

import numpy as np

def angular_dist(r1, d1, r2, d2):
  # 각도를 라디안으로
  r1, d1 = np.radians(r1), np.radians(d1)
  r2, d2 = np.radians(r2), np.radians(d2)

  a = np.sin(np.abs(d1-d2)/2)**2
  b = np.cos(d1) * np.cos(d2) * np.sin(np.abs(r1-r2)/2)**2
  d = 2 * np.arcsin(np.sqrt(a+b))
  # 다시 라디안을 각도로
  return np.degrees(d)








# 데이터 불러와서 좌표 계산하기

def import_bss():
  data = np.loadtxt('bss.dat', usecols=range(1,7))
  res = []
  for i, row in enumerate(data):
    hms = hms2dec(row[0], row[1], row[2])
    dms = dms2dec(row[3], row[4], row[5])
    res.append((i+1, hms, dms))
  return res

def import_super():
  data = np.loadtxt('super.csv', delimiter=',', skiprows=1, usecols=[0, 1])
  res = []
  for i, row in enumerate(data):
    res.append((i+1, row[0], row[1]))
  return res








# 가까운 물체 찾기

import sys
def find_closest(cat, r, d):
  res_id = None
  res_dist = np.inf
  for row in cat:
    dist = angular_dist(row[1], row[2], r, d)
    if dist < res_dist:
      res_dist = dist
      res_id = row[0]
  return (res_id, res_dist)
