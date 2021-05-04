using System;

class Program
{

    public static void Main()
    {
        int[] array = new int[7] { 24, 17, 27, 3, 19, 15, 22 };
        int minimum = findExtremum(array, smaller);
        int maximum = findExtremum(array, bigger);
        Console.WriteLine("陣列中最小值為:" + minimum);
        Console.WriteLine("陣列中最大值為:" + maximum);
        Console.Read();
    }

    delegate int compare(int x, int y);

    static int smaller(int x, int y)
    {
        if (x < y)
            return x;
        return y;
    }
    static int bigger(int x, int y)
    {
        if (x > y)
            return x;
        return y;
    }

    static int findExtremum(int[] arr, compare comp)
    {
        int extremum = arr[0];
        for (int i = 1; i < arr.Length; ++i)
            extremum = comp(extremum, arr[i]);
        return extremum;
    }
}

