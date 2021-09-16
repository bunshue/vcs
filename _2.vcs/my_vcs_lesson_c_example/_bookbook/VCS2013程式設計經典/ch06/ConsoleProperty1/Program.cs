using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleProperty1
{
    class Car
    {
        public int Speed; 	// 宣告Speed為public公用變數
    }

    class Program
    {
        static void Main(string[] args)
        {
            Car Benz = new Car();
            Benz.Speed = 100;	// 物件建立之後可直接使用「.」存取該屬性
            Console.WriteLine("Benz.Speed = {0} ",Benz.Speed);
            Console.Read();

        }
    }
}
