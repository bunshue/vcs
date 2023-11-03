using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CH0307
{
    class Program
    {
        static void Main(string[] args)
        {
            //32_985為 C# 7.0的語法         
            int x = 32_985, y = 147;
            //設定輸出格式，D5表示5位整數，不止者前方補零
            Console.WriteLine($"x = {x}, y = {y:D5}");
            //設定輸出格式，N0表示輸出不含小數的數值，加千位符號
            Console.WriteLine($"x += y, x = {x += y:N0}");
            Console.WriteLine($"x *= y, x = {x *= y:N0}");

            x = 32_985; //重設變數x的值
            Console.WriteLine($"x %= y, x = {x %= y}");

            string word = "Mid-Autumn";
            word += " Festival";
            Console.WriteLine(word);

            Console.ReadKey();   //螢幕暫停
        }
    }
}
