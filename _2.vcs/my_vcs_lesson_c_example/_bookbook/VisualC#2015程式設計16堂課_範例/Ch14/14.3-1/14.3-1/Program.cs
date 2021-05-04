using System;
using CatTest;

class Program
{
    public static void Main()
    {
        Cat kitty = new Cat();
        kitty.name = "凱蒂";
        Cat doraemon = new Cat("多啦A夢", "機器貓");
        doraemon.setweight(129);
        Cat garfield = new Cat("加菲", "虎斑貓");
        garfield.setweight(5);

        kitty.print();
        doraemon.print();
        garfield.print();
        Console.WriteLine();

        garfield.feed();
        doraemon.play();
        Console.WriteLine();

        kitty.print();
        doraemon.print();
        garfield.print();

        Console.Read();
    }
}

