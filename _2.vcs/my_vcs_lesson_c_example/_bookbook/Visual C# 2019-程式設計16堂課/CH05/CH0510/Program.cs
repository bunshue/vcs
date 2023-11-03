using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//滙入靜態類別

namespace CH0510
{
    class Program
    {
        static void Main(string[] args)
        {
            //宣告字元陣列，每一列有3個元素
            char[][] ch = new char[][]
            {  new char[] {'A', 'b', 'C', 'd'},
            new char[] {'e', 'f', 'g'},
            new char[] {'T', 'W', 'X', 'Y', 'Z'}};

            WriteLine("鋸齒陣列的字元：");

            //外層for廻圈讀取列數，ch.Length取得列數
            for (int outer = 0; outer < ch.Length; outer++)
            {
                //內層for廻圈讀取欄數，ch[outer].Length取得欄數
                for (int inner = 0;
                      inner < ch[outer].Length; inner++)
                {
                    Write($" {ch[outer][inner]}");
                }
                WriteLine();   //換行
            }

            ReadKey();//螢幕暫停
        }
    }
}