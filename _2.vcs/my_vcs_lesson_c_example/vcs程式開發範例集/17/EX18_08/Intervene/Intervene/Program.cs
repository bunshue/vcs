using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Intervene
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] iArrary = new int[] { 1, 13, 3, 6, 10, 55, 98, 2, 87, 12, 34, 75, 33, 47 };
            InsertionSorter ii = new InsertionSorter();
            ii.Sort(iArrary);
            for (int m = 0; m < iArrary.Length; m++)
                Console.Write("{0} ", iArrary[m]);
            Console.ReadLine();
        }
    }
}
