using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleMethod1
{
    class Program
    {
        // 定義Login方法，傳回型別為void，表示呼叫此方法不傳回值
        // 呼叫Login方法時，第一個引數需傳入字串資料，第二個引數需傳入布林資料
        private static void Login(string username, bool ismale)
        {
            Console.Write(username);
            if (ismale)
            {
                Console.WriteLine("先生，歡迎光臨！");
            }
            else
            {
                Console.WriteLine("小姐，歡迎光臨！");
            }
        }

        static void Main(string[] args)
        {
            string name = "王小華";
            // 呼叫Login方法
            // 傳入的第一個參數為name變數，第二個參數為true
            Login(name, true);
            Console.WriteLine();
            // 呼叫Login方法，傳入第一個參數是字串資料，第二個參數為false
            Login("李美美", false);
            Console.Read();
        }
    }
}
