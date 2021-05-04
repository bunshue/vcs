using System;
using AnimalSpace;

class Program
{
    public static void Main()
    {
        Human myself = new Human("小李", "亞洲人", 64, 172);
        Cat mypet = new Cat("喵仔", "暹邏貓", 7, 30, 20);
        myself.setpet(mypet);

        myself.print();
        Console.WriteLine("類型為:" + myself.gettype());
        Console.WriteLine();

        Console.WriteLine("他的寵物是:");
        myself.getpet().print();
        mypet.print_length();

        Console.Read();
    }
}

