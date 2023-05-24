# 교차 매칭 - 넘파이


import time
import numpy as np
def angular_dist(r1, d1, r2, d2):
  a = np.sin(np.abs(d1-d2)/2)**2
  b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1-r2)/2)**2
  return 2*np.arcsin(np.sqrt(a+b))

# 단위가 헷갈림.
# 전체를 일단 라디안으로 변환.
# matches에 거리를 기록할 때는 다시 디그리로 변환.


def crossmatch(cat1, cat2, max_dist):
  start = time.time()
  # cat1, cat2, max_dist 모두 라디안으로 변환
  max_dist = np.radians(max_dist)
  cat1 = np.radians(cat1)
  cat2 = np.radians(cat2)

  matches = []
  no_matches = []
  
  for id1, (r1, d1) in enumerate(cat1):
    min_id = None
    min_dist = np.inf
    for id2, (r2, d2) in enumerate(cat2):
      dist = angular_dist(r1, d1, r2, d2)
      if dist < min_dist:
        min_id = id2
        min_dist = dist
    
    if min_dist > max_dist:
      no_matches.append(id1)
    else:
      # 여기서 min_dist를 다시 degrees로 변환.
      matches.append((id1, min_id, np.degrees(min_dist)))
    
  end = time.time() - start

  return matches, no_matches, end






# 넘파이로 더 빠르게.

def crossmatch(cat1, cat2, max_dist):
  start = time.time()
  max_dist = np.radians(max_dist)
  cat1 = np.radians(cat1)
  cat2 = np.radians(cat2)
  matches = []
  no_matches = []
  
  # r2들을 리스트로 뽑고, d2들을 리스트로 뽑기!
  r2_list = cat2[:,0]
  d2_list = cat2[:,1]

  for id1, (r1, d1) in enumerate(cat1):
    # dist도 리스트로 나옴.
    dist = angular_dist(r1, d1, r2_list, d2_list)
    min_dist = np.min(dist)
    min_id = np.argmin(dist)
    
    if min_dist > max_dist:
      no_matches.append(id1)
    else:
      matches.append((id1, min_id, np.degrees(min_dist)))
    
  end = time.time() - start

  return matches, no_matches, end