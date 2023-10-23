using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace Exchange
{
    class Program
    {
        static void Main(string[] args)
        {
            int num, hundred, fifty, ten;
            Write("請輸入將兌換金額:");
            num = int.Parse(ReadLine());
            hundred = num / 100;
            fifty = (num - hundred * 100) / 50;
            ten = (num - hundred * 100 - fifty * 50) / 10;
            WriteLine("百元鈔有" +hundred +"張 五十元鈔有"+ fifty+ "張 十元硬幣有" + ten +"個");
            Read();
        }
    }
}
