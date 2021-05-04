using System;

class Program
{
    public static void Main()
    {
        Console.WriteLine("   1  2  3  4  5  6  7  8  9");

        for (int i = 1; i <= 9; i++)
        {
            Console.Write(i);
            for (int j = 1; j <= 9; j++)
            {
                Console.Write((i * j).ToString().PadLeft(3));
            }
            Console.WriteLine();
        }
        Console.Read();
    }
}

