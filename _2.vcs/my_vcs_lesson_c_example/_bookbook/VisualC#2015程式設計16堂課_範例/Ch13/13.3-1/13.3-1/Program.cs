using System;

class Program
{

    public static void Main()
    {
        try
        {
            Console.Write("請輸入被除數");
            int x = int.Parse(Console.ReadLine());
            Console.Write("請輸入除數");
            int y = int.Parse(Console.ReadLine());
            Console.WriteLine("商為: " + x / y + "餘數為: " + x % y);
        }
        catch (Exception ex)
        {
            Console.WriteLine("\n例外發生");
            Console.WriteLine("訊息: " + ex.Message);
            Console.WriteLine("例外來源: " + ex.Source);
            Console.WriteLine("丟出例外的方法: " + ex.TargetSite);
            Console.WriteLine("詳細文字說明: " + ex.ToString());
        }

        Console.Read();
    }

}

