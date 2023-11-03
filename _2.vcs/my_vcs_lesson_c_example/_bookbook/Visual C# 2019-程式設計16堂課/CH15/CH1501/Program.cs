using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using static System.Console;

namespace CH1501
{
    class Program
    {
        static void Main(string[] args)
        {
            //設定檔案的路徑
            string path = @"D:\C#Lab\CH15\Program.cs";
            string append = @"D:\C#Lab\CH15\final.txt";
            string str;
            int index = 1;

            StreamReader sr = File.OpenText(path);
            StreamWriter sw = File.AppendText(append);

            while ((str = sr.ReadLine()) != null)
            {
                WriteLine($"{index:D5} {str}");
                sw.WriteLine($"{index++:D5} {str}");
            }
            sr.Close();
            sw.Close();
            ReadKey();
        }
    }
}
