using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace Shift
{
    class Program
    {
        static void Main(string[] args)
        {
            int a = 8888;

            WriteLine(a + "<<5=" + (a << 5) ); //左移運算  
            WriteLine(a + ">>5=" + (a >> 5));  // 右移運算 
            Read();
        }
    }
}
