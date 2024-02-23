amount=int(input("請輸入需繳費金額:"))
money=int(input("請輸入付款金額:"))

change=temp=money-amount    	#change與temp為找零
n500=change//500       		#change除於500取得500元張數再指定給n500 
change=change%500      		#求500元張數後剩於的找零
n100=change//100       		#change除於100取得100元張數再指定給n100
change=change%100      		#求100元張數後剩於的找零
n50=change//50         		#change除於50取得50元個數再指定給n50
change=change%50       		#求50元張數後剩於的找零
n10=change//10         		#change除於10取得10元個數再指定給n10
change=change%10       		#求10元張數後剩於的找零
n5=change//5           		#change除於5取得5元個數再指定給n5
change=change%5        		#求5元張數後剩於的找零
n1=change//1           		#change除於1取得1元個數再指定給n1
print("收您{}元，找您{}元".format(money, temp))	#顯示繳費金額與找零金額
print("500元{}張\n100元{}張\n 50元{}個\n 10元{}個\n  5元{}個\n  1元{}個"
 	.format(n500,n100,n50,n10,n5,n1))
