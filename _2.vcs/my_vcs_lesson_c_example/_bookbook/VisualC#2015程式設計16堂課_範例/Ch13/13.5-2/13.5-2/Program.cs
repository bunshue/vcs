using System;

class Program
{

    public static void Main()
    {
        int year = 0, month = 0, day = 0;
        DateTime birth = new DateTime();

        try
        {
            Console.Write("請輸入生日西元紀年: ");
            year = check("year", int.Parse(Console.ReadLine()));
            Console.Write("請輸入生日月份: ");
            month = check("month", int.Parse(Console.ReadLine()));
            Console.Write("請輸入生日日期: ");
            day = check("day", int.Parse(Console.ReadLine()));
            birth = new DateTime(year, month, day);
        }
        catch (ArgumentOutOfRangeException ex)
        {
            Console.WriteLine("您輸入的數值不合理");
        }
        catch (Exception ex)
        {
            Console.WriteLine("發生其他例外，例外訊息: " + ex.Message);
        }

        TimeSpan age = DateTime.Now - birth;
        Console.WriteLine("您約為" + age.Days / 365.0 + "歲, 共" + age.Days + "天");
        Console.Read();
    }

    public static int check(string type, int value)
    {
        switch (type)
        {
            case "year":
                if (value > DateTime.Now.Year)
                    throw new ArgumentOutOfRangeException();
                break;
            case "month":
                if (value > 12 || value < 1)
                    throw new ArgumentOutOfRangeException();
                break;
            case "day":
                if (value > 31 || value < 1)
                    throw new ArgumentOutOfRangeException();
                break;
        }
        return value;
    }

}

