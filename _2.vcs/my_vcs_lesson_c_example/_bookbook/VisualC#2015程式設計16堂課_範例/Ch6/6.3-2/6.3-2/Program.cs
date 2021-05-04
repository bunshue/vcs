using System;

class Program
{
    public static void Main()
    {
        Console.WriteLine("請輸入0~100一個任意數字");
        int input = int.Parse(Console.ReadLine());

        for (int i = 1; i < 100; i++)
        {
            Console.WriteLine(i);
            if (i == input)
                break;
        }

        Console.Read();
    }
}

