using System;

class Program
{
    public static void Main()
    {
        Console.Write("請輸入欲計算階乘的數字: ");
        int number;
        number = int.Parse(Console.ReadLine());

        double sum = 1;
        for (; number > 1; --number)
            sum *= number;

        Console.WriteLine("階乘結果為: " + sum);
        Console.Read();
    }
}

