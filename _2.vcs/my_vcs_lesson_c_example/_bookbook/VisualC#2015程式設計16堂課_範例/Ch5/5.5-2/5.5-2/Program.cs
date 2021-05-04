using System;

class Program
{
    public static void Main()
    {
        int total;
        Console.Write("請輸入消費總額 ");
        total = int.Parse(Console.ReadLine());

        int count = 0;
        if (total % 10 == 7)
            count++;
        if ((total / 10) % 10 == 7)
            count++;
        if ((total / 100) % 10 == 7)
            count++;

        switch (count)
        {
            case 1:
                Console.WriteLine("該筆消費將以95折計算");
                Console.WriteLine("折扣後金額為: " + total * 0.95 + "元");
                break;
            case 2:
                Console.WriteLine("該筆消費將以8折計算");
                Console.WriteLine("折扣後金額為: " + total * 0.8 + "元");
                break;
            case 3:
                Console.WriteLine("該筆消費將以6折計算");
                Console.WriteLine("折扣後金額為: " + total * 0.6 + "元");
                break;
            default:
                Console.WriteLine("該筆消費不符合折扣條件, 將以原價 " + total + "元計價");
                break;
        }

        Console.Read();
    }
}

