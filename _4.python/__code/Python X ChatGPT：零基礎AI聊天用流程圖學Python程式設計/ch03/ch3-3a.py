score1 = 35
score2 = 10
score3 = 10
score2 = 27
print("第一節 = ", score1, "(", id(score1), ")")
print("第二節 = ", score2, "(", id(score2), ")")
print("第三節 = ", score3, "(", id(score3), ")")
print("=======================================")
score3 = score2
print("第一節 = ", score1, "(", id(score1), ")")
print("第二節 = ", score2, "(", id(score2), ")")
print("第三節 = ", score3, "(", id(score3), ")")