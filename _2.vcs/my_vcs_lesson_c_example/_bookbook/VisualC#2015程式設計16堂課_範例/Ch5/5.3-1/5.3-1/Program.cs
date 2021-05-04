using System;

class Program
{
    public static void Main()
    {
        int gender, height, weight;

        Console.WriteLine("男生請輸入1，女生請輸入2");
        gender = int.Parse(Console.ReadLine());
        Console.WriteLine("請輸入您的身高(cm)");
        height = int.Parse(Console.ReadLine());
        Console.WriteLine("請輸入您的體重(kg)");
        weight = int.Parse(Console.ReadLine());

        double high = 0, low = 0;
        if (gender == 1)
        {
            high = (height - 80) * (0.7) * (1.1);
            low = (height - 80) * (0.7) * (0.9);
        }
        else if (gender == 2)
        {
            high = (height - 70) * (0.6) * (1.1);
            low = (height - 70) * (0.6) * (0.9);
        }
        Console.WriteLine("您的理想體重範圍為: " + low + " ~ " + high + " kg");

        if (weight < low)
            Console.WriteLine("您的體重屬於「過輕」的範圍");
        else if (weight > high)
            Console.WriteLine("您的體重屬於「過重」的範圍");
        else
            Console.WriteLine("您的體重屬於「正常」的範圍");

        Console.Read();
    }
}
