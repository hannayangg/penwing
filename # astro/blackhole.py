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