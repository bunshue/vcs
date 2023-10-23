using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace StringMethod
{
    class Program
    {
        static void Main(string[] args)
        {
            string str1 = "圖解資料結構";
            string str2 = "程式範例實作";
            string str3 = "使用C++";
            string str4 = "使用Java";
            string str;
            str = str1 + str2;
            WriteLine("字串串接：" + str);
            WriteLine("字串長度：" + str.Length);
            str = str.Insert(12, str3);
            WriteLine("字串插入：" + str);
            WriteLine("字串長度：" + str.Length);
            str = str.Replace(str1, str4);
            WriteLine("字串取代：" + str);
            WriteLine("字串長度：" + str.Length);
            str = str.Remove(2, 4);
            WriteLine("字串刪除：" + str);
            WriteLine("字串長度：" + str.Length);
            Read(); //暫停
        }
    }
}
