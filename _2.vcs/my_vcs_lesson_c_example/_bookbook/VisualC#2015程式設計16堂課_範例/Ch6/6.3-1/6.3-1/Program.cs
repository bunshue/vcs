using System;

class Program
{
    public static void Main()
    {
        Console.WriteLine("請輸入一個1~9之間的數字");
        int input = int.Parse(Console.ReadLine());

        Console.WriteLine("以下是1~100中含有" + input + "的數字");
        for (int i = 1; i < 100; i++)
        {
            if (i % 10 != input && i / 10 != input)
                continue;
            Console.WriteLine(i);
        }

        Console.Read();
    }
}

