using System;

class Program
{

    public static void Main()
    {
        Console.WriteLine("兩整數(2與3)相加: " + sum(2, 3));
        Console.WriteLine("三整數(1與2與3)相加: " + sum(1, 2, 3));
        Console.WriteLine("兩double型態(0.2與0.3)相加: " + sum(0.2, 0.3));

        int[] array = new int[] { 1, 2, 3, 4, 5 };
        Console.WriteLine("整數陣列(1,2,3,4,5)總和: " + sum(array));
        Console.Read();
    }

    public static int sum(int x, int y)
    {
        return x + y;
    }

    public static int sum(int x, int y, int z)
    {
        return x + y + z;
    }

    public static double sum(double x, double y)
    {
        return x + y;
    }

    public static int sum(int[] arr)
    {
        int total = 0;
        for (int i = 0; i < arr.Length; ++i)
            total += arr[i];
        return total;
    }
}

