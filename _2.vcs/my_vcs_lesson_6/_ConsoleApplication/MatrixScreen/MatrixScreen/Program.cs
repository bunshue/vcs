using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MatrixScreen
{
    class Program
    {
        static void Main(string[] args)
        {
            //set text color
            Console.ForegroundColor = ConsoleColor.Green;

            Random rand = new Random();

            String str = "";

            Console.Write("Press ENTER to start...");
            Console.ReadKey();
            for (int i = 0; i < 20000; i++)
            {
                //create new string pattern
                if (i % 2 == 0)
                {
                    str = "";
                    for (int j = 0; j < 79; j++)
                    {
                        int n = rand.Next(5);
                        if (n < 2)
                        {
                            str += n.ToString();
                        }
                        else
                        {
                            str += " ";
                        }
                    }
                }
                Console.WriteLine(str);
            }
            Console.WriteLine("End of screen...");
            Console.Write("Press any key to exit...");
            Console.ReadKey();
        }
    }
}
