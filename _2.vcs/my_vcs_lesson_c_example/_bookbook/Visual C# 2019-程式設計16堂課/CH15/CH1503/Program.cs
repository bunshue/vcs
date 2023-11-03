using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using static System.Console;

namespace CH1503
{
    class Program
    {
        static void Main(string[] args)
        {
            string path = @"D:\C#Lab\Sample\Demo.txt";
            string str;
            FileStream fs = new FileStream(path,
               FileMode.OpenOrCreate, FileAccess.Write);
            StreamWriter sw = new StreamWriter(
               fs, Encoding.Unicode);
            WriteLine("請輸入想儲存的文字");
            str = ReadLine();
            sw.WriteLine(str);  //將資料寫入檔案
            sw.Close();   //關閉sw資料流
            WriteLine("檔案內所輸入的文字為");
            FileStream f = new FileStream(path,
               FileMode.OpenOrCreate, FileAccess.Read);
            StreamReader sr = new StreamReader(
               f, Encoding.Unicode);
            sr.BaseStream.Seek(0, SeekOrigin.Begin);
            while (sr.Peek() > -1)
            {
                WriteLine(sr.ReadLine());//讀出檔案
            }
            sr.Close();  //關閉資料流
            ReadKey();
        }
    }
}
