using System;

class Program
{

    public static void Main()
    {
        try
        {
            Console.Write("請輸入生日西元紀年: ");
            int year = int.Parse(Console.ReadLine());
            int age = verify(year);
            Console.WriteLine("您已成年, 今年" + age + "歲");
        }
        catch (ArgumentOutOfRangeException ex)
        {
            Console.WriteLine("您並未成年");
        }
        catch (ArgumentException ex)
        {
            Console.WriteLine("您輸入的年份範圍不合理");
        }
        catch (Exception ex)
        {
            Console.WriteLine("發生其他例外，例外訊息: " + ex.Message);
        }

        Console.Read();
    }

    public static int verify(int year)
    {
        if (year < 1 || year > DateTime.Now.Year)
            throw new ArgumentException();
        else if (DateTime.Now.Year - year < 18)
            throw new ArgumentOutOfRangeException();
        else
            return DateTime.Now.Year - year;
    }

}

