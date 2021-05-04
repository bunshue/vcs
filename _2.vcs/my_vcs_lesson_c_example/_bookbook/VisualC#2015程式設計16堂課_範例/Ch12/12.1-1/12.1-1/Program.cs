using System;

class Program
{
    public static void Main()
    {
        Console.Write("請輸入欲階乘的數字: ");
        int input = int.Parse(Console.ReadLine());

        bool valid = checkRange(input, 0, 16);
        if (valid)
            Console.WriteLine("階乘結果為: " + factorial(input));
        else
            Console.WriteLine("負數或階乘結果會超出整數型態範圍");

        Console.Read();
    }

    public static bool checkRange(int check, int min, int max)
    {
        if (check < min)
            return false;
        else if (check > max)
            return false;
        else
            return true;
    }

    public static int factorial(int num)
    {
        int result = 1;
        for (int i = 1; i <= num; ++i)
            result *= i;
        return result;
    }

}

