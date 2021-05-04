using System;

class Program
{

    public static void Main()
    {
        bool success = test();
        if (success)
            Console.WriteLine("測試區塊已正常執行");
        else
            Console.WriteLine("測試區塊有例外發生");
        Console.Read();

    }

    public static bool test()
    {
        int[] array = new int[] { 1, 2, 3, 4, 5, 6 };
        Console.Write("請輸入0~5之間的陣列位置: ");
        try
        {
            int x = int.Parse(Console.ReadLine());
            Console.WriteLine("陣列在該位置的值為: " + array[x]);
            return true;
        }
        catch (FormatException ex)
        {
            Console.WriteLine("輸入格式錯誤, 無法成功轉換為整數型態");
            return false;
        }
        catch (IndexOutOfRangeException ex)
        {
            Console.WriteLine("輸入數字超出陣列範圍");
            return false;
        }
        finally
        {
            Console.WriteLine("測試區塊執行結束");
        }
    }
}

