using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Choice
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] iArrary = new int[] { 1, 5, 3, 6, 10, 55, 9, 2, 87, 12, 34, 75, 33, 47 };
            SelectionSorter ss = new SelectionSorter();
            ss.Sort(iArrary);
            for (int m = 0; m < iArrary.Length; m++)
            {
                Console.Write("{0} ", iArrary[m]);
            }
            Console.ReadLine();
        }
    }
}
