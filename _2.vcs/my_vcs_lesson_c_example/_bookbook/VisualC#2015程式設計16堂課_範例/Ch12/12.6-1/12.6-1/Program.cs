using System;

class Program
{

    public static void Main()
    {
        Console.Write("請輸入第一個數字: ");
        int x = int.Parse(Console.ReadLine());
        Console.Write("請輸入第二個數字: ");
        int y = int.Parse(Console.ReadLine());

        int gcd = GCD(x, y);
        Console.WriteLine("最大公因數為: " + gcd);
        Console.Read();
    }

    public static int GCD(int a, int b)
    {
        Console.WriteLine("(" + a + ", " + b + ")");
        b = b % a;
        if (b == 0)
            return a;
        return GCD(b, a);
    }

}

