using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace LeapYear
{
    class Program
    {
        static void Main(string[] args)
        {
            int year = 2008;//西元年
                            //宣告整數變數
            if (year % 4 != 0)   /*如果year不是4的倍數*/
                WriteLine(year + " 年不是潤年。"); /*則顯示year不是潤年*/
            else if (year % 100 == 0)  /*如果year是100的倍數*/
            {
                if (year % 400 == 0)      /*且year是400的倍數*/
                    WriteLine(year + " 年是潤年。");
                /*顯示year是潤年*/
                else      /*否則*/
                    WriteLine(year + " 年不是潤年。");
                /*則顯示year不是潤年*/
            }
            else  /*否則*/
                WriteLine(year + " 年是潤年。"); /*則顯示year是潤年*/
            Read();
        }
    }
}
