using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace 字串串接
{
    class Program
    {
        static void Main(string[] args)
        {
            string str1, str2, str3;
            str1 = "Time";
            str2 = " Creates";
            str3 = " Hero";
            str1 = str1 + str2 + str3;  //將字串串接
            WriteLine(str1); //顯示
            Read(); //暫停
        }
    }
}