using System;

class Program
{
    public static void Main()
    {
        int i = 0;

        while (i < 5)
        {
            Console.WriteLine("進入了while迴圈");
            i++;
        }

        do
        {
            Console.WriteLine("進入了do...while迴圈");
        } while (i < 5);
        Console.Read();
    }
}

