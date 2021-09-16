using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleEx1
{
    class Program
    {
        static void Main(string[] args)
        {
            // 宣告字串資料型別ProductName變數，用來存放品名
            string ProductName;
            // 宣告整數資料型別Price變數，用來存放單價
            int Price;
            Console.Write("請輸入品名：");        // 印出 "請輸入品名："
            // 由鍵盤輸入品名資料並按 [Enter]鍵，即將品名存放至ProductName變數
            ProductName = Console.ReadLine();
            Console.Write("請輸入單價：");         // 印出 "請輸入單價："
            // 由鍵盤輸入單價並按 [Enter]鍵，將單價轉成整數之後
            // 再將單價放至Price變數
            Price = int.Parse(Console.ReadLine());
            Console.WriteLine("品名：{0}　單價：{1}　這筆記錄儲存成功",ProductName, Price);
            Console.Read();

        }
    }
}
