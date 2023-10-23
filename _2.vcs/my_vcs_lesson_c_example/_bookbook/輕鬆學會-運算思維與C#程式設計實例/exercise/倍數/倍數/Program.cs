using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//滙入靜態類別

namespace 倍數
{
    class Program
    {
        static int a1;
        static void onehundred()
        {
            WriteLine("100倍的結果為：{0}", a1 * 100);
        }

        static void Main(string[] args)
        {
            Write("請輸入一個數字：");
            a1 = int.Parse(ReadLine());
            onehundred();
            Read();
        }
    }
}
