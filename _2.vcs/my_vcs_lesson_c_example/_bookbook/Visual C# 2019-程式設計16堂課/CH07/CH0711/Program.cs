using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0711
{
    class Program
    {
        //靜態方法
        static void Lotto(ref byte[] anyArr)
        {
            //以Random類別呼叫NextBytes()方法產生隨機數
            Random rand = new Random();
            //建立能存放6個元素的陣列
            anyArr = new byte[6];
            rand.NextBytes(anyArr);
        }

        static void Main(string[] args)
        {
            byte[] number = new byte[6];
            //呼叫靜態方法，以陣列為引數
            Lotto(ref number);
            Console.WriteLine("今天的樂透--");
            //讀取陣列元素
            foreach (byte item in number)
            {
                Console.Write($"{item}, 3");
            }
            Console.ReadKey();
        }
    }
}