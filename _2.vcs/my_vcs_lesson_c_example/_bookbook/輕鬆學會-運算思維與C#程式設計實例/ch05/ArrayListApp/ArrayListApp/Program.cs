using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Collections;
using static System.Console;  //滙入靜態類別

namespace ArrayListApp
{
    class Program
    {
        static void Main(string[] args)
        {
            ArrayList animal = new ArrayList();
            string name_of_animal;
            WriteLine("請輸入動物名稱(輸入 # 結束輸入)：");
            do
            {
                Write("===: ");
                name_of_animal = ReadLine();
                animal.Add(name_of_animal);
            } while (name_of_animal != "#");
            WriteLine("共輸入" + (animal.Count - 1) + "筆資料：");
            WriteLine("最後一筆輸入符號 # 為結束輸入的字元");
            foreach (string temp in animal)
            {
                Write("-->");
                WriteLine(temp);
            }
            WriteLine();
            Read(); //暫停
        }
    }
}
