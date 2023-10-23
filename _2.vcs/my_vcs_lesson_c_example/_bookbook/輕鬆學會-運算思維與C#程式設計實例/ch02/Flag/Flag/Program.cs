using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace Flag
{
    class Program
    {
        static void Main(string[] args)
        {
            int x;

            x = (765 / 17 +1)* 2 * 210;
            WriteLine("共需花費:"+x+ "元");
            Read();

        }
    }
}
