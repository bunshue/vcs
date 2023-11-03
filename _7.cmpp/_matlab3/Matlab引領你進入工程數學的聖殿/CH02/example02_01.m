year=input('請輸入您需查詢的年份：');                     
n=weekday([int2str(year),'-4-30']);            
day=1+(14-n);                                  
fprintf('%d年的母親節日期：%d-%d-%d\n',year,year,5,day)
