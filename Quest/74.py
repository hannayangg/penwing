# [74. leetcode 242]


def F(s, t):
  return sorted(s) == sorted(t)



import collections
def F(s, t):
    return collections.Counter(s) == collections.Counter(t)

#  _   _                         __ __
# | |_| |___ _ _ ___ _ ___ ___ _/  '  \
# |  _  / _ ' | /   | /   / _ ' \     / 
# |_| |_\___,_|__|__|__|__\___,_,\___/
#  _   _             ____     _ 
# | |_| |___ _ _ ___/  __\___| |
# |  _  / _ ' | /   |__  / _ \ | 
# |_| |_\___,_|__|__|____\___/_|
print('s')
