using System;

class Program
{

    public static void Main()
    {
        Random rnd = new Random();
        int answer = rnd.Next(1, 100);

        Console.WriteLine("電腦已亂數產生一個範圍在1~99的整數");
        Console.Write("請輸入您的猜測: ");

        int guess = int.Parse(Console.ReadLine());
        while (guess != answer)
        {
            if (guess > answer)
                Console.WriteLine("您猜的答案太大了!");
            else
                Console.WriteLine("您猜的答案太小了!");
            Console.Write("請輸入您的猜測: ");
            guess = int.Parse(Console.ReadLine());
        }
        Console.WriteLine("恭喜您猜中答案了!");

        Console.Read();
    }

}

