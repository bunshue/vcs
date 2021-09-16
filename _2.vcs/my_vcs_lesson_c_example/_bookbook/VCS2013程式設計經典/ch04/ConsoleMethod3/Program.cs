using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleMethod3
{

    // 定義Class1類別，此類別內含公開的GetWelcome靜態方法
    class Class1
    {
        public static string GetWelcome(string username, bool ismale)
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
            return str;  // 傳回字串
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            string name = "王小華";
            //使用Class1類別的GetWelcome方法
            string Welcome = Class1.GetWelcome(name, true);
            Console.WriteLine(Welcome);
            Console.WriteLine();
            Console.WriteLine(Class1.GetWelcome("李美美", false));
            Console.Read();
        }
    }
 }
