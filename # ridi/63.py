# [63 색 정렬]

def F(nums):
  nums.sort()


# 책 풀이 - 퀵정렬인데 잘 모르겠음!
# red:0, white:1, blue:2

def F(nums):
  red, white, blue = 0, 0, len(nums)
  while white < blue:
    if nums[white] < 1:
      nums[red], nums[white] = nums[white], nums[red]
      white += 1
      red += 1
    elif nums[white] > 1:
      blue -= 1
      nums[white], nums[blue] = nums[blue], nums[white]
    else:
      white += 1