using System;

class Program
{

    public static void Main()
    {
        Console.Write("請輸入您欲計算的費式數列項數: ");
        int x = int.Parse(Console.ReadLine());
        Console.WriteLine("費式數列第" + x + "項為: " + fibonacci(x));
        Console.Read();
    }

    public static int fibonacci(int n)
    {
        if (n == 1 || n == 2)
            return 1;
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}

