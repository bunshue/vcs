using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleProperty3
{

     class Car       // 定義Car類別
    {
        private int _angle = 10; // 私有_angle變數初值為10
        public int Angle    	// 定義Angle唯讀屬性
        {						// Angle屬性只有get區段沒有set區段
            get
            {
                return _angle;
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Car Benz = new Car();
            Console.WriteLine("Benz.Angle = {0}",Benz.Angle);  // Angle只能讀不能寫
            Console.Read();
        }
    }
}
