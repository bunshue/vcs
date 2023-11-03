using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//滙入靜態類別

namespace CH0413
{
    class Program
    {
        static void Main(string[] args)
        {
            WriteLine("輸入兩個數值，取得它們的最大公因數");
            Write("第一個數值：");
            int num1 = int.Parse(ReadLine());
            Write("第二個數值：");
            int num2 = int.Parse(ReadLine());
            Write($"{num1}、{num2}的");
            //被除數num2不能為0
            while (num2 != 0)
            {
                //取得餘數
                int remain = num1 % num2;
                //將被除數、餘數做置換動作
                num1 = num2; //被除數num2更換成除數num1
                num2 = remain;//將前式所得餘數更換為被除數
            }
            WriteLine($"GCD = {num1}");
            ReadKey();//螢幕暫停
        }
    }
}
