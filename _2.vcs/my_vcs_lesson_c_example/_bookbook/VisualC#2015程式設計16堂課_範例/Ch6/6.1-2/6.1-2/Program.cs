using System;

class Program
{
    public static void Main()
    {
        int i, sum = 0;
        for (i = 0; i <= 10; i++)
            sum += i;

        Console.WriteLine("級數總和為: " + sum);
        Console.Read();
    }
}

