using System;

class Program
{
    public static void Main()
    {
        int[] array = new int[5];
        array[0] = 1;
        array[2] = 3;
        array[3] = 4;

        for (int i = 0; i < 5; i++)
            Console.WriteLine(array[i]);
        Console.Read();
    }
}

