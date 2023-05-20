# 교차매칭


import numpy as np
import time
def crossmatch(cat1, cat2, max_dist):
  start = time.time()
  max_dist = np.radians(max_dist)

  matches = []
  no_matches = []

  # convert coordinates to radians
  cat1 = np.radians(cat1)
  cat2 = np.radians(cat2)

  for id1, (r1, d1) in enumerate(cat1):
    # 가장 가까운 각거리 & 후보
    min_dist = np.inf
    min_id2 = None

    for id2, (r2, d2) in enumerate(cat2):
      a = np.sin(np.abs(d1-d2)/2)**2
      b = np.cos(d1) * np.cos(d2) * np.sin(np.abs(r1-r2)/2)**2
      dist = 2 * np.arcsin(np.sqrt(a+b))
      # 가장 가까운 각거리 & 후보 업데이트
      if dist < min_dist:
        min_id2 = id2
        min_dist = dist
    
    # 가장 가까운 각거리가 임계거리보다 작으면 통과!
    if min_dist > max_dist:
      no_matches.append(id1)
    else:
      matches.append((id1, min_id2, np.degrees(min_dist)))
      
  end = time.time() - start
  return matches, no_matches, end