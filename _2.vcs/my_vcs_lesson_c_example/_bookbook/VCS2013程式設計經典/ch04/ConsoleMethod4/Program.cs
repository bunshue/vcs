using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleMethod4
{
    // 定義Class1類別內含公開的GetWelcome方法
    // 呼叫GetWelcome方法時必須先建立Class1類別物件
    class Class1
    {
        public string GetWelcome(string username, bool ismale)
        {
            string str = "";
            if (ismale)
            {
                str = username + "先生，歡迎光臨！";
            }
            else
            {
                str = username + "小姐，歡迎光臨！";
            }
            return str;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            string name = "王小華";
            // 建立myClass物件為Class1類別
            Class1 myClass = new Class1();
            // 呼叫Class1類別的GetWelcome方法
            string Welcome = myClass.GetWelcome(name, true);
            Console.WriteLine(Welcome);
            Console.WriteLine();
            Console.WriteLine(myClass.GetWelcome("李美美", false));
            Console.Read();
        }
    }

}
