using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CH0803
{
    class Program
    {
        static void Main(string[] args)
        {
            Mother woman = new Mother();
            woman.Display();
            Child tomas = new Child();
            tomas.Show();
            Console.ReadKey();
        }
    }
}
