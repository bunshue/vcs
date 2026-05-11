def print_msg():
    print("歡迎學習Python程式設計!")

def sum_to_ten():
    s = 0   
    for i in range(1, 11):
        s += i
    print("從1加到10 = " + str(s))

print_msg()
sum_to_ten()
