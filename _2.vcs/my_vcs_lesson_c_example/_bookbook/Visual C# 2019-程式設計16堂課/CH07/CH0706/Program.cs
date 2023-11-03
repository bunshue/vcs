using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CH0706
{
    class Program
    {
        //宣告靜態方法
        static void randNum(out byte[] figures)
        {
            //以Random類別呼叫NextBytes()方法產生隨機數
            Random rand = new Random();
            //建立能存放5個元素的陣列
            figures = new byte[5];
            rand.NextBytes(figures);
        }

        //宣告靜態方法，以out來修飾變數
        static void Show()
        {
            //宣告Anynum陣列並以out參數傳遞同時進行
            randNum(out byte[] Anynum);
            //讀取陣列元素
            foreach (byte item in Anynum)
                Console.Write($"{item,-4}");
        }

        static void Main(string[] args)
        {
            Console.Write("隨機數：");
            Show();
            Console.ReadKey();
        }
    }
}
