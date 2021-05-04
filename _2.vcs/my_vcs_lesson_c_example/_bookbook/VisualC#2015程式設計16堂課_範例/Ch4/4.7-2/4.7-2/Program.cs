using System;

class Program
{
    public static void Main()
    {
        int total, highscore, score;

        Console.WriteLine("請輸入國文成績");
        score = int.Parse(Console.ReadLine());
        total = highscore = score;

        Console.WriteLine("請輸入英文成績");
        score = int.Parse(Console.ReadLine());
        total += score;
        highscore = score > highscore ? score : highscore;

        Console.WriteLine("請輸入數學成績");
        score = int.Parse(Console.ReadLine());
        total += score;
        highscore = score > highscore ? score : highscore;

        Console.WriteLine("三科總分為: " + total);
        Console.WriteLine("三科平均為: " + Convert.ToDouble(total) / 3);
        Console.WriteLine("最高分為: " + highscore);

        Console.Read();
    }
}

