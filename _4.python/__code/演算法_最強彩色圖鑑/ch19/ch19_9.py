# ch19_9.py
def climbStairs(n):
    prev, cur = 1, 1
    for i in range(1, n):
        prev, cur = cur, prev + cur         
    return cur

print(climbStairs(2))
print(climbStairs(3))
print(climbStairs(4))










      



    





        





