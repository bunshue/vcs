# ch11_8.py
def interest(interest_type, subject = '敦煌'):
    """ 顯示興趣和主題 """
    print("我的興趣是 " + interest_type )
    print("在 " + interest_type + " 中, 最喜歡的是 " + subject)
    print( )

interest('旅遊')                                     # 傳遞一個參數
interest(interest_type = '旅遊')                     # 傳遞一個參數
interest('旅遊', '張家界')                           # 傳遞二個參數
interest(interest_type = '旅遊', subject = '張家界') # 傳遞二個參數
interest(subject = '張家界', interest_type = '旅遊') # 傳遞二個參數
interest('閱讀', '旅遊類')                # 傳遞二個參數,不同的主題




    
