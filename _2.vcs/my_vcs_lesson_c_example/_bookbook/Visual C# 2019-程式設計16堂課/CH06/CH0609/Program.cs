using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CH0609
{
    class Program
    {
        static void Main(string[] args)
        {
            Dinner first = new Dinner("百匯沙拉");
            first.showInfo();
            Dinner second = new Dinner("義大利麵", "綠茶");
            second.showInfo();
            Dinner third = new
               Dinner("焗烤茄蔬", "咖啡", "涼拌小菜");
            third.showInfo();
            Console.ReadKey();
        }
    }
}
