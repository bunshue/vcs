using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleMethod2
{
    class Program
    {
        // 定義GetWelcome方法，該方法傳回型別為string 字串
        private static string GetWelcome(string username, bool ismale)
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

        static void Main(string[] args)
        {
            string name = "王小華";
            //將方法傳回的結果指定給Welcome變數
            string Welcome = GetWelcome(name, true);
            Console.WriteLine(Welcome);
            Console.WriteLine();
            Console.WriteLine(GetWelcome("李美美", false));
            Console.Read();
        }
    }
}
