import numpy as np




def F(nums, B):
  
  mean = np.mean(nums, axis=0)
  std = np.std(nums, axis=0)
  min_val = mean-std
  max_val = mean+std
  width = 2*std/B

  m, n = nums[0].shape
  leftbins = np.zeros((m, n))
  bins = np.zeros((m, n, B))
  for num in nums:
      for i in range(m):
          for j in range(n):
              if num[i][j] < min_val[i][j]:
                  leftbins[i][j] += 1
              elif num[i][j] < max_val[i][j]:
                  idx = int((num[i][j]-min_val[i][j])/width[i][j])
                  bins[i][j][idx] += 1

  return (mean, std, leftbins, bins)








def _F(nums, B):
  mean, std, leftbins, bins = F(nums, B)
  min_val = mean-std
  max_val = mean+std
  width = 2*std/B

  # 데이터 전체의 개수 N
  N = len(nums)

  # mid
  mid = (N+1)/2
  
  # 미디언 배열 (2,3)
  m = bins.shape[0]
  n = bins.shape[1]
  median = np.zeros((m, n))

  for i in range(m):
    for j in range(n):
      count = leftbins[i][j]
      for b, bincount in enumerate(bins[i][j]):
        count += bincount
        
        # 임계 넘을 때까지 누적
        if count >= mid:
          med = min_val[i][j] + (b+0.5)*width[i][j]
          median[i][j] = med
          break
  return median










# (2,3)배열, bins=5 -> 각 원소에 bins 5개씩 들어감.
nums1 = np.array([[1,1,1],
                  [1,1,1]])
nums2 = np.array([[2,2,2],
                  [2,2,2]])
nums3 = np.array([[3,3,3],
                  [3,3,3]])
nums4 = np.array([[4,4,4],
                  [4,4,4]])
nums5 = np.array([[5,5,5],
                  [5,5,5]])
nums6 = np.array([[6,6,6],
                  [6,6,6]])
nums7 = np.array([[7,7,7],
                  [7,7,7]])
nums8 = np.array([[8,8,8],
                  [8,8,8]])
nums9 = np.array([[9,9,9],
                  [9,9,9]])
nums10 = np.array([[10,10,10],
                   [10,10,10]])

nums = [nums1, nums2, nums3, nums4, nums5, nums6, nums7, nums8]
B = 3

_F(nums, B)