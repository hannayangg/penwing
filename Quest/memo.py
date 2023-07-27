import numpy as np
# 7 ~ 8    1개
# 8 ~ 9    3개 누적4개
# 9 ~ 10   5개 누적9개
# 10 ~ 11  9개 누적18개 따라서 10.5를 중앙값으로 추정.
# 11 ~ 12  4개
# 12 ~ 13  5개
# 13 ~ 14  2개
# 15 ~ 16  1개

nums = [7,8,8,8,9,9,9,9,9,
        10,10,10,10,10,10,10,10,10,
        11,11,11,11,
        12,12,12,12,12,
        13,13,
        16]

# 중앙값 = 15.5번째 숫자.
median = (nums[14] + nums[15]) // 2
print(median)

# 구간별개수, 구간정보
hist, bin_edges = np.histogram(nums, bins=9)

# 구간별개수 누적 리스트
hist_cumsum = np.cumsum(hist)
print(hist_cumsum)

# 중앙값 추정 = 구간별 개수가 15.5개가 넘을 때의 구간으로 추정.
idx = np.argmax(hist_cumsum > 15.5)
print(idx)
print(bin_edges[idx], bin_edges[idx+1])


def median_approx(nums, B):
    hist, bin_edges = np.histogram(nums, bins=B)
    if len(nums) % 2 == 0:
        m = (len(nums)//2) + 0.5
    else:
        m = len(nums)//2
    hist_cumsum = np.cumsum(hist)
    idx = np.argmax(hist_cumsum > m)
    median = (bin_edges[idx] + bin_edges[idx+1]) / 2
    return median

def median_bins(nums, B):
    hist, bin_edges = np.histogram(nums, bins=B)
    mean = np.mean(nums)
    std = np.std(nums)
    numbers = len(np.argwhere(nums < mean-std))

    return mean, std, numbers, hist

median_bins([1, 5, 7, 7, 3, 6, 1, 1], 4)
median_approx([1, 5, 7, 7, 3, 6, 1, 1], 4)

