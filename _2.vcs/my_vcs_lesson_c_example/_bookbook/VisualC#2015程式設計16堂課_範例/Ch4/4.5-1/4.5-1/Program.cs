using System;

class Program
{
    public static void Main()
    {
        int radius;
        const float pi = 3.14159F;

        Console.WriteLine("請輸入半徑");
        radius = int.Parse(Console.ReadLine());

        Console.WriteLine("所求圓周為" + radius * 2 * pi);
        Console.Read();
    }
}

