using System;
using myStack;

class Program
{
    public static void Main()
    {
        Stack stack = new Stack(5);

        Console.WriteLine("Push 13");
        stack.Push(13);
        Console.WriteLine("Push 22");
        stack.Push(22);
        Console.WriteLine("Push 24");
        stack.Push(24);

        Console.WriteLine("Pop! " + stack.Pop());
        Console.WriteLine("Push 27");
        stack.Push(27);
        Console.WriteLine("Pop! " + stack.Pop());
        Console.WriteLine("Pop! " + stack.Pop());

        Console.Read();
    }
}

