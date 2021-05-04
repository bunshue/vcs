using System;

class Program
{

    public static void Main()
    {
        int[] array = new int[] { 1, 2, 3, 4, 5, 6 };

        Console.Write("請輸入0~5之間的陣列位置: ");
        int x = int.Parse(Console.ReadLine());
        Console.WriteLine("陣列在該位置的值為: " + array[x]);
        Console.Read();
    }

}

