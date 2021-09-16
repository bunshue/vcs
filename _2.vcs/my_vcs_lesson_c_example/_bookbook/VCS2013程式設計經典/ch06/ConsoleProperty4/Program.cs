using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleProperty4
{
    class Car   // 定義Car類別
    {
      private bool _turbo = false;
      public bool Turbo   	// 定義Turbo唯寫屬性
      {						// Turbo屬性只有set區段沒有get區段
         set
         {
           _turbo = value;
         }
      }
    }

    class Program
    {
        static void Main(string[] args)
        {
           Car Benz = new Car();
           Benz.Turbo = true;      // Turbo屬性只能寫不能讀
           //Console.WriteLine (" {0}", Benz.Turbo );
           //Console.read();

        }
    }
}
