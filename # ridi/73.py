# [73 UTF-8 검증]


# 내가 푼 것. 좀 어거지임.

# 1) count == 1 : 첫 글자가 0b10으로 시작, False
# 2) count >= 5 : 111110xx 같은 수는 없음, False
# 바이트 수는 4까지만 있음 (561p 표)

def F(data):
  def _F(nums): # 바이트 수 = 1의 개수
    p = 0
    while p < len(nums) and nums[p] == '1':
      p += 1
    return p
    
  while data:
    p = data.pop(0)
    b = "{0:b}".format(p).zfill(8)
    bites = _F(b)

    if (bites > 4) or (bites == 1 and b[0] == '1'): # 가능한 바이트 수: 1~4
      return False
    for _ in range(bites-1):
      if not data or "{0:b}".format(data[0]).zfill(8)[:2] != '10':
        return False
      data.pop(0)
  return True


# 책 풀이
# bin으로 안바꿔도 됨. (왜지?)
# 8자리 중, 0x, 110x, 1110x, 11110x 만으로 판별하려면, 뒤에 날리는 것(>>) 필요.
# 197 = 0b11000101임. 뒤에 5개 날려서 197>>5 == 0b110.

def F(data):
  def check(size):
    for i in range(idx+1, idx+1+size):
      if i >= len(data) or data[i]>>6 != 0b10:
        return False
    return True
  idx = 0
  while idx < len(data):
    if data[idx]>>7 == 0b0:
      idx += 1
    elif data[idx]>>5 == 0b110 and check(1):
      idx += 2
    elif data[idx]>>4 == 0b1110 and check(2):
      idx += 3
    elif data[idx]>>3 == 0b11110 and check(3):
      idx += 4
    else:
      return False
  return True