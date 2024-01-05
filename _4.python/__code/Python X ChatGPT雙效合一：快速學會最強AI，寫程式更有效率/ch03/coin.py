print("請輸入將兌換金額: ",end="")
num=int(input())
hundred=num//100
fifty=(num-hundred*100)//50
ten=(num-hundred*100-fifty*50)//10
print("百元鈔有%d張 五十元鈔有%d張 十元鈔有%d張" %(hundred,fifty,ten))
