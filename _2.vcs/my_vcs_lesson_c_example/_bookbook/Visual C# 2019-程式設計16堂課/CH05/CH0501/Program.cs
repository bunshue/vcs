using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//滙入靜態類別


namespace CH0501
{
    class Program
    {
        static void Main(string[] args)
        {
            //建立陣列後，指定索引存放資料
            int[] number = new int[4];
            WriteLine($"陣列第一個元素 {number[0] = 123} ");
            WriteLine($"指定第三個元素 {number[2] = 456} ");
            WriteLine($"陣列第四個元素 {number[3]}");

            //陣列初始化之後，配合索引取得陣列存放的資料
            int[] score = new int[] { 65, 92, 73, 84 };
            WriteLine($"國文 {score[0]}");
            WriteLine($"數學 {score[2]}");

            ReadKey();//螢幕暫停
        }
    }
}
