score1 = 35
score2 = 10
score3 = 10
score2 = 27
print("第一節 = " + str(score1) + "(" + str(id(score1)) + ")")
print("第二節 = " + str(score2) + "(" + str(id(score2)) + ")")
print("第三節 = " + str(score3) + "(" + str(id(score3)) + ")")
print("=======================================")
score3 = score2
print("第一節 = " + str(score1) + "(" + str(id(score1)) + ")")
print("第二節 = " + str(score2) + "(" + str(id(score2)) + ")")
print("第三節 = " + str(score3) + "(" + str(id(score3)) + ")")