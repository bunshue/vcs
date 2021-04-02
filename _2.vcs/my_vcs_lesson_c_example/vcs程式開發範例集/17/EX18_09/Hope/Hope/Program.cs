using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Hope
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] iArrary = new int[] { 1, 5, 13, 6, 10, 55, 99, 2, 87, 12, 34, 75, 33, 47 };
            ShellSorter sh = new ShellSorter();
            sh.Sort(iArrary);
            for (int m = 0; m < iArrary.Length; m++)
                Console.Write("{0} ", iArrary[m]);
            Console.ReadLine();
        }
    }
}
