# [중앙값 추정]


import numpy as np






def median_bins(nums, B):
  mean = np.mean(nums)
  std = np.std(nums)
  min_val = mean-std
  max_val = mean+std
  # 구간너비 = 최소+최대 / 구간개수
  width = 2*std/B
  

  # bins 만들기
  left_bins = 0 # 작은 원소 개수(개)
  bins = np.zeros(B)

  for n in nums:
    if n < min_val:
      left_bins += 1
    elif n < max_val:
      # 기준점으로부터 위치 / 구간너비
      idx = int((n-min_val)/width)
      bins[idx] += 1
  
  return mean, std, left_bins, bins





# nums가 10개라면
# 작은 수부터 시작하여 5.5개를 넘어갈 때를 찾아야 함.
# 임계 개수를 넘어갈 때의 인덱스 찾기.


def median_approx(nums, B):
  mean, std, left_bins, bins = median_bins(nums, B)
  width = 2*std/B
  
  # 임계 개수
  mid = (len(nums)+1)/2
  
  # 작은 원소 개수
  count = left_bins

  for b, bincount in enumerate(bins):
    count += bincount
    # 임계개수를 넘을 때까지 개수를 누적
    if count >= mid:
      break
  
  median = (mean-std) + width*b + width*0.5
  return median