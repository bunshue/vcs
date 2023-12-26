# ch11_25_5e.py
def lazy_evaluation(expression):
    def evaluate():
        print(f'評估 : {expression}')
        return eval(expression)
    return evaluate

lazy_sum = lazy_evaluation('1 + 2 + 3 + 4')     # 這裡不會立即計算總和

result = lazy_sum()                             # 這裡將計算並返回總和
print(result)                               

