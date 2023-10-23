using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace Jagged
{
    class Program
    {
        static void Main(string[] args)
        {
            int[][] number = new int[][]
                  {   new int[] {10,40,60},
                new int[] {302,45,56,108,560,32},
                new int[] {100,150,200,500}};

            for (int i = 0; i < 3; i = i + 1)
            {
                for (int j = 0; j < number[i].Length; j = j + 1)
                {
                    Write("[{0}]", number[i][j]);
                }
                WriteLine();
            }
            Read();
        }
    }
}
