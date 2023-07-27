# [20. leetcode 39]


# 내가 푼 것
def F(nums, target):
    res = []
    def _F(path, idx):
        # 종료 조건
        if sum(path)>target: return
        if sum(path)==target:
            res.append(path)
            return
        
        # BT
        for i in range(idx, len(nums)):
          _F(path+[nums[i]], i)
    _F([], 0)
    return res





# neetcode
def F(nums, target):
    res = []
    def _F(path, i):
        # 종료 조건
        if i>=len(nums): return 
        if sum(path)>target: return
        if sum(path)==target:
            res.append(path)
            return
        
        # BT
        _F(path+[nums[i]], i)
        _F(path, i+1)
    _F([], 0)
    return res