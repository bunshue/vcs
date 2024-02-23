# ch19_10.py
def rob(nums):
    prev = cur = 0
    for money in nums:
        prev, cur = cur, max(prev + money, cur)
    return cur

print(rob([1, 2, 3, 1]))
print(rob([2, 7, 9, 3, 1]))










      



    





        





