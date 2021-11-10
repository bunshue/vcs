using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace vcs_MyClassLibrary
{
    public class Class1
    {
    }

    public class MyClass
    {
        public static void show()
        {
            Console.WriteLine("歡迎來到vcs");
        }
        public static void show(string message)
        {
            Console.WriteLine(message);
        }

        public static double rad(double d)
        {
            return d * Math.PI / 180.0;
        }

        public static double sind(double d)
        {
            return Math.Sin(d * Math.PI / 180.0);
        }

        public static double cosd(double d)
        {
            return Math.Cos(d * Math.PI / 180.0);
        }
    }

}
