using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace Escape
{
    class Program
    {
        static void Main(string[] args)
        {
            WriteLine("\"\x48\x41\x50\x50\x59\"");
            Read(); //暫停
        }
    }
}
