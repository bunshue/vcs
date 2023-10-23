using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace UseMethod
{
    class Program
    {
        static int total, temp;

        //計算整數次方總和的方法,參數i表示次方數
        public static int Total(uint i, params int[] num)
        {
            total = temp = 0;

            for (int t = 0; t < num.Length; t++)  //處理加總的動作
            {
                temp = num[t];
                for (int k = 1; k < i; k++)        //處理次方相乘的動作
                {
                    temp *= num[t];
                }
                total += temp;
            }
            return total;
        }

        static void Main(string[] args)
        {
            //以變數c儲存方法的單一傳回值
            WriteLine("請依序輸入三個數字: ");
            Write("第一個數字=> ");
            int num1 = int.Parse(ReadLine());
            Write("第二個數字=> ");
            int num2 = int.Parse(ReadLine());
            Write("第三個數字=> ");
            int num3 = int.Parse(ReadLine());

            int c = Total(3, num1, num2, num3);

            WriteLine("{0}的立方+{1}的立方+{2}的立方三者之總和={3} ", num1, num2, num3, c);
            ReadLine();
        }
    }
}
