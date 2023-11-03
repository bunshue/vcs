using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//滙入靜態類別

namespace CH0507
{
    class Program
    {
        static void Main(string[] args)
        {
            ArrayList name = new ArrayList();
            string str_tmp;
            WriteLine("請輸入學生姓名(按 . 結束輸入)：");

            do
            {
                Write(">");
                //讀取輸入資料，以Add()方法加到陣列中
                str_tmp = ReadLine();
                name.Add(str_tmp);
            } while (str_tmp != ".");

            WriteLine($"共輸入{(name.Count - 1)}筆資料：");

            //foreach廻圈讀取陣列元素
            foreach (string str_tmp1 in name)
            {
                Write("-->");
                WriteLine(str_tmp1);
            }
            WriteLine();

            ReadKey();//螢幕暫停
        }
    }
}
