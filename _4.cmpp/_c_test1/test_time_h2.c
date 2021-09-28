#include <stdio.h>
#include <time.h>

int main()
{
    //time() 回傳日曆時間，也就是自 1970 年 1 月 1 日後經過的總秒數。
    printf("使用time()\n");
    time_t tt = time(NULL);
    printf("自 1970 年 1 月 1 日後經過了 %d 秒....\n\n", tt);

    //localtime() 以指向日曆時間的指標 (pointer) 當作參數 (parameter) ，將此日曆時間轉換成結構 (structure) tm 的表示方法，並回傳表示此結構 tm 。
    printf("使用localtime()\n");
    struct tm *nPtr1 = localtime(&tt);
    int year = nPtr1->tm_year + 1900;
    int month = nPtr1->tm_mon + 1;
    int mday = nPtr1->tm_mday;
    int wday = nPtr1->tm_wday;
    printf("今天是 %u 年 %u 月 %u 號星期 %u\n\n", year, month, mday, wday);

    //asctime() 將結構 (structure) tm 中所表示的時間格式轉換成字串 (string) ，因此以指向結構 tm 的指標 (pointer) 當作參數，回傳表示此時間格式的字串 (string) 。
    printf("使用asctime()\n");
    struct tm *nPtr2 = localtime(&tt);
    char *now1 = asctime(nPtr2);
    printf(now1);
    printf("\n");

    //ctime() 將日曆時間轉換成字串 (string) ，因此以指向日曆時間的指標 (pointer) 當作參數 (prameter) ，回傳表示此時間格式的字串。
    printf("使用ctime()\n");
    char *now2 = ctime(&tt);
    printf(now2);
    printf("\n");


    //strftime() 將結構 (structure) tm 中的時間格式轉換成指定格式的字串 (string) ，有各種可指定的轉換格式
    printf("使用localtime()\n");
    struct tm *nPtr3 = localtime(&tt);
    char now3[30];
    strftime(now3, 30, "%Y %B %d %A", nPtr3);
    printf("%s\n\n", now3);


    //clock() 回傳程式執行後佔用的 CPU 時間，單位為 tick 。
    printf("使用clock()做delay 1.23秒 測試\n");
    long waittime = CLOCKS_PER_SEC * 1.23;

    printf("等待 %d msec\n", waittime);
    while (clock() < waittime)
    {

    }

    printf("時間到~~~~~\n\n");


    return 0;
}





