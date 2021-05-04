using System;

class Program
{
    static int pos_num = 0, pos_total = 0;
    static int neg_num = 0, neg_total = 0;

    public static void Main()
    {
        Console.WriteLine("請輸入五個數字");
        for (int i = 0; i < 5; ++i)
            Console.WriteLine(check(int.Parse(Console.ReadLine())));

        Console.WriteLine("共輸入了" + pos_num + "個正數");
        Console.WriteLine("共輸入了" + neg_num + "個負數");
        Console.WriteLine("總和為: " + (pos_total + neg_total));

        Console.Read();
    }

    public static string check(int x)
    {
        if (x > 0)
            return pos(x);
        else if (x < 0)
            return neg(x);
        else
            return "=0";
    }

    public static string pos(int x)
    {
        ++pos_num;
        pos_total += x;
        return "正數";
    }

    public static string neg(int x)
    {
        ++neg_num;
        neg_total += x;
        return "負數";
    }
}

