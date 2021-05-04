using System;

class Program
{
    public static void Main()
    {
        int x = 0, y = 0;
        Console.WriteLine("變數x的起始值為: " + x);
        Console.WriteLine("變數y的起始值為: " + y);

        increase(x, ref y);
        Console.WriteLine("Call-by-Value的結果, x為: " + x);
        Console.WriteLine("Call-by-Reference的結果, y為: " + y);

        Console.Read();
    }

    public static void increase(int a, ref int b)
    {
        a = a + 1;
        b = b + 1;
    }

}

