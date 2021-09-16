using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleStruct1
{
    class Program
    {
        // 定義Product產品結構資料型別
        struct Product
        {
            // Product產品結構內含No編號欄位、Name品名欄位、Price單價欄位
            public string No, Name;
            public int Price;
       }

       static void Main(string[] args)
        {
            // 宣告game結構變數為Product結構型別
             Product game;
            // 設定game.No編號欄位的值為 "G01"
            game.No = "G01";
            // 設定game.Name品名欄位的值為"XBox One"
            game.Name = "XBox One";
            // 設定game.Price單價欄位的值為10000
            game.Price = 10000;
            Product cookie;        // 宣告cookie結構變數為Product結構型別
            Console.Write(" 請輸入產品編號：");
            // 由鍵盤輸入編號再指定給cookie.No編號欄位
            cookie.No = Console.ReadLine();
            Console.Write(" 請輸入產品名稱：");
            // 由鍵盤輸入品名再指定給cookie.Name品名欄位
            cookie.Name = Console.ReadLine();
            Console.Write(" 請輸入產品單價：");
            // 由鍵盤輸入單價並轉成整數再指定給cookie.Price單價欄位
            cookie.Price = int.Parse(Console.ReadLine());
            Console.WriteLine();
            Console.WriteLine(" ====== 產品單價清單 ====== ");
            Console.WriteLine();
            // 印出game及cookie結構的編號、品名及單價
            Console.WriteLine(" 產品編號：{0} ", game.No);
            Console.WriteLine(" 產品名稱：{0} ", game.Name);
            Console.WriteLine(" 產品單價：{0} ", game.Price);
            Console.WriteLine(" 產品編號：{0} ", cookie.No);
            Console.WriteLine(" 產品名稱：{0} ", cookie.Name);
            Console.WriteLine(" 產品單價：{0} ", cookie.Price);
            Console.Read();
        }
    }
}
