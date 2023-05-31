# [14. leetcode 190]


def F(n):
  n = bin(n)
  n = ''.join(list(reversed(n))[:-2])
  plus = '0'*(32-len(n))
  n += plus
  return int(n, 2)



def F(n):
  res = 0
  for i in range(n):
    bit = (n>>i) & 1
    res = res | (bit << (31-i))
  return res



# 뒤서부터 bit'1' 찾기 (AND; 1&1=1 이용)
# 00...010"1" & 1 => bit = 00...000"1" = 1.
# 00...01"0"  & 1 => bit = 00...00"0"  = 0.
# 00...0"1"   & 1 => bit = 00...0"1"   = 1.

# 앞서부터 bit'1' 추가 (OR; 0|1=1 이용)
# res = 00....000
# bit = "1"0....000
# OR  = "1"000..000