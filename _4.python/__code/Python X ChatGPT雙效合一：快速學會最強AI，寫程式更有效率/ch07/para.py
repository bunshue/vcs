def square_sum(*arg):
    ans=0
    for n in arg:
        ans += n*n
    return ans

ans1=square_sum(1)
print('1*1=',ans1)
ans2=square_sum(1,2)
print('1*1+2*2=',ans2)
ans3=square_sum(1,2,3)
print('1*1+2*2+3*3=',ans3)
ans4=square_sum(1,3,5,7)
print('1*1+3*3+5*5+7*7=',ans4)

def progname(**arg):
    return arg

print(progname(d1='python', d2='java', d3='visual basic'))
