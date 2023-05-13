import numpy as np
nums = [1,1,3,2,2,6]
B = 3

mean = np.mean(nums)
std = np.std(nums)
width = 2*std/B


left_bin = 0
for n in nums:
    if n < mean-std: left_bin += 1

bins, bin_edges = np.histogram(nums,bins=B, range=(mean-std, mean+std))
print(bins)

mid = len(nums) / 2

cumsum = np.cumsum(bins[left_bin:])
print(cumsum)
b = np.argmax(cumsum >= mid)
print(b)

median = mean - std + width*(b + 0.5)

print(median)