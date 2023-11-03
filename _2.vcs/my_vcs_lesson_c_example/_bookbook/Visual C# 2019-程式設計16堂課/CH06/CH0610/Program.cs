using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0610
{
    class Program
    {
        static void Main(string[] args)
        {
            WriteLine($"沒有物件，汽車 {Motor.Number} 輛");
            Motor sienta = new Motor("Sienta", 1.5F);
            Motor yaris = new Motor("Yaris", 1.8F);
            Motor hybrid = new Motor("Hybrid", 2.0F);
            ReadKey();
        }
    }
}
