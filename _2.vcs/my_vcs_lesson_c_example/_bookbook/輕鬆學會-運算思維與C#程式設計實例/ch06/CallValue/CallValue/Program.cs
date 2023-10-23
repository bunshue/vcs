using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace CallValue
{
    class Program
    {
        public static void One_hundred(int a, int b, int c)
        {
            a = 100 * a;
            b = 100 * b;
            c = 100 * c;
            WriteLine("方法內變成100倍的值 a={0} b={1} c={2}", a, b, c);
        }

        static void Main(string[] args)
        {
            int a = 1;        //a,b,c為Main()方法中的區域變數
            int b = 2;
            int c = 3;

            WriteLine("程式呼叫前 a={0} b={1} c={2}", a, b, c);
            One_hundred(a, b, c);   //傳入固定長度參數
            WriteLine("程式呼叫後 a={0} b={1} c={2}", a, b, c);
            Read();
        }
    }
}