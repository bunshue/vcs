import twstock
from twstock import BestFourPoint

stock = twstock.Stock("2330") 
bfp = BestFourPoint(stock)

bfp_buy = bfp.best_four_point_to_buy()
print("是否為四大買點:", bfp_buy)
bfp_sell = bfp.best_four_point_to_sell()
print("是否為四大賣點:", bfp_sell)
bfp_result = bfp.best_four_point()
print("綜合判斷:", bfp_result)
