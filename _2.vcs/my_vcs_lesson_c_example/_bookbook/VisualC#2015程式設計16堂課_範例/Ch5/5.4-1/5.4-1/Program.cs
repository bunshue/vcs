using System;

class Program
{
    public static void Main()
    {
        int a;
        Console.WriteLine("請輸入第一個數字");
        a = int.Parse(Console.ReadLine());

        String ope;
        Console.WriteLine("請輸入運算符號");
        ope = Console.ReadLine();

        int b;
        Console.WriteLine("請輸入第二個數字");
        b = int.Parse(Console.ReadLine());

        switch (ope)
        {
            case "+":
                Console.WriteLine("運算結果為 " + (a + b));
                break;
            case "-":
                Console.WriteLine("運算結果為 " + (a - b));
                break;
            default:
                Console.WriteLine("我不認識這個運算符號...");
                break;
        }

        Console.Read();
    }
}

