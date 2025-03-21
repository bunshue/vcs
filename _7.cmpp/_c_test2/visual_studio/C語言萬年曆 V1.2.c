//C語言萬年曆 V1.2
// http://www.itkee.com/developer/detail-bb9.html
/*
[項目]用C語言編寫萬年曆
      1、輸入年份，判斷是否�d閏年
      2、輸入年月日，判斷改日�d星期幾
      3、輸入年份，打出12個月曆，輸入月份，打出該月的日曆
      4、要求用多個函數實現
===============================
[名稱]萬年曆
[版本]Ver 1.2
[修改]1、對輸入的日期進行容錯處理
      2、增加和修改�d英文的月份和星期顯示
      3、採用指針形式的weeks和month數組
[日期]20:09 2010-6-14
*/

#include <stdio.h>
#include <conio.h>   //getch(); tolower(); exit();
#include <stdlib.h> //system();

int days[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
char *weeks[7] ={"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
char *months[12] = {"January", "February", "March", "April", "May", "June",
                    "July", "August", "September", "October", "November", "December"};

bool isLeap(int year) //by theLeap(); theCalendar();
{
    if(year%4 == 0 && year%100 != 0 || year%400 == 0) return true;
    else return false;
}
void theLeap() //by Select();
{
    int year;
    printf("\nPlease input the year: ");
    scanf("%d", &year);
    if( isLeap( year ) ) { printf("\nThe year %d is leap year.", year); }
    else { printf("\nThe year %d is not leap year.", year); }
    getch();
}
int Zeller(int year, int month, int day) //by theWeek(); printCalendar();
{
    int c, y, m, d, w;
    if( month < 3) { year -= 1; month += 12; }
    c = year / 100;
    y = year % 100;
    m = month;
    d = day;
    w = y + y/4 + c/4 - 2*c + 26*(m+1)/10 + d - 1;
    w %= 7;
    return (w >= 0 ? w : w+7);
}
void theWeek() //by Select();
{
    int year, month, day, w;
    printf("\n");
    do
    {
        printf("Please input the date(YYYY-MM-DD): ");
        scanf("%d-%d-%d", &year, &month, &day);
        if( isLeap( year ) ) days[1] = 29; //是否閏年
        else days[1] = 28;
    }while(!( (month > 0 && month < 13) && (day > 0 && day <= days[month - 1]) ) );

    w = Zeller(year, month, day);

    printf("\nThis day %d-%02d-%02d is %s.", year, month, day, weeks[w]);
    getch();
}
void printCalendar(int year, int month) //by details(); theCalendar();
{
    int w, d;
    w = Zeller(year, month, 1);
    printf("%28s", months[month - 1]);
    printf("\n            -%02d-\n", month);
    printf(" SUN MON TUE WED THU FRI SAT\n");
    for(d = 0; d < w; d++) { printf("    "); }
    for(month--, d = 1; d <= days[month]; d++)
    {
        printf("%4d", d);
        if( (d + w)%7 == 0 && d != days[month]) printf("\n");
    }
    printf("\n============================\n");
}
void details(int year) //by theCalendar();
{
    int month;
    while(true)
    {
        do
        {
            system("cls");
            printf("Press '0' to exit.\n");
            printf("Please input the month: ");
            scanf("%d", &month);
        }while(!(month >=0 && month <= 12));
        if(month != 0)
        {
            printf("\n");
            printf("Calendar                %d\n", year);
            printCalendar(year, month);
            if( getch() == '0') break;
        }
        else break;
    }
}
void theCalendar() //by Select();
{
    int year, month;
    printf("\nPlease input the year: ");
    scanf("%d", &year);
    if( isLeap( year ) ) days[1] = 29; //是否閏年
    else days[1] = 28;

    system("cls");
    printf("Calendar                %d\n", year);
    for(month = 1; month <= 12; month++)
    {
        printCalendar(year, month);
    }

    printf("More details of each month ?[Y/N]");
    if( tolower(getch()) == 'y' ) details( year );
}
void Menu() //by main();
{
    system("cls");
    printf("1 -This year is leap year or not\n");
    printf("2 -This day is which day of the week\n");
    printf("3 -The calendar of this year\n");
    printf("0 -Exit\n\n");
    printf("Please select the options:");
}
void Select() //by main();
{
    char key;
    bool v = true;
    while( v )
    {
        key = getch();
        switch( key )
        {
        case '1': theLeap(); v = false; break;
        case '2': theWeek(); v = false; break;
        case '3': theCalendar(); v = false; break;
        case '0': exit(1);
        }
    }
}
int main(void)
{
    while(true) { Menu(); Select(); }
    return 0;
}


