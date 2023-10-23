using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace Dim3
{
    class Program
    {
        static void Main(string[] args)
        {
            int number = 0;
            int[,,] Test = new int[2, 3, 4];
            for (int i = 0; i < 2; i = i + 1)
            {
                for (int j = 0; j < 3; j = j + 1)
                {
                    for (int k = 0; k < 4; k = k + 1)
                    {
                        Test[i, j, k] = number;
                        number = number + 1;
                    }
                }
            }
            WriteLine("==========================");
            for (int i = 0; i < 2; i = i + 1)
            {
                for (int j = 0; j < 3; j = j + 1)
                {
                    Write("Test[");
                    for (int k = 0; k < 4; k = k + 1)
                    {
                        Write(" {0:D2}", Test[i, j, k]);
                    }
                    Write("]");
                    WriteLine();
                    WriteLine("==========================");
                }
                WriteLine();
            }
            Read();
        }
    }
}
