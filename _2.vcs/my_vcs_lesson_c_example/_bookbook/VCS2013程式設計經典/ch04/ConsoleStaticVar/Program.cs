using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleStaticVar
{
    class Class1
    {
        private static int age = 29;
        public static string name = "陳春嬌";
    }

    class Program
    {
        private static int age = 25;
        private static string name = "王志明";
        static void Main(string[] args)
        {
            Console.WriteLine("Program類別靜態變數的資訊-->{0}的年齡為{1}歲\n",
            name, age.ToString());
            Console.WriteLine("Class1類別靜態變數的資訊-->{0}的年齡無法取得",
               Class1.name);
            Console.Read();
        }
    }
}
