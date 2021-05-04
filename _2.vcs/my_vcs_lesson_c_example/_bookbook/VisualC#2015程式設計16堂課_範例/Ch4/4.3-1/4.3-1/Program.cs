using System;

class Program
{
    public static void Main()
    {
        int integer;
        float floating;

        Console.WriteLine("請輸入一任意整數");
        integer = int.Parse(Console.ReadLine());
        Console.WriteLine("請輸入一任意浮點數(小數)");
        float.TryParse(Console.ReadLine(), out floating);

        Console.WriteLine("您輸入的整數是" + integer);
        Console.WriteLine("您輸入的浮點數是" + floating);

        integer = Convert.ToInt32(floating);
        Console.WriteLine("您輸入的浮點數轉換為整數後是" + integer);

        Console.Read();
    }
}

