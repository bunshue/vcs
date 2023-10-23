using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace StringFormat
{
    class Program
    {
        static void Main(string[] args)
        {
            //** 日期時間輸出

            WriteLine(String.Format("{0:dddd, MMM d yyyy}", DateTime.Now));
            WriteLine(String.Format("{0:HH:mm:ss}", DateTime.Now));
            WriteLine(String.Format("{0:D}", DateTime.Now));
            WriteLine(String.Format("{0:hh:mm:ss tt}", DateTime.Now));
            WriteLine(String.Format("{0:T}", DateTime.Now));
            WriteLine(String.Format("{0:h:m:s}", DateTime.Now));

            //** 自訂格式化輸出
            WriteLine(String.Format("{0:##,##0.00}", 8567.1));
            WriteLine(String.Format("{0:###0.00}", 566.7));
            WriteLine(String.Format("{0:0.00%}", 8));
            Read(); //暫停
        }
    }
}
