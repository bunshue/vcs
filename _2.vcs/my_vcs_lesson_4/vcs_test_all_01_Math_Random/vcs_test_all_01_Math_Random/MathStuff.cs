using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace vcs_test_all_01_Math_Random
{
    public class MathStuff
    {
        // Return the greatest common divisor (GCD) of a and b.
        public static long GCD(long a, long b)
        {
            // Make a >= b.
            a = Math.Abs(a);
            b = Math.Abs(b);
            if (a < b)
            {
                long tmp = a;
                a = b;
                b = tmp;
            }

            // Pull out remainders.
            for (; ; )
            {
                long remainder = a % b;
                if (remainder == 0) return b;
                a = b;
                b = remainder;
            }
        }

        // Return the least common multiple of a and b.
        public static long LCM(long a, long b)
        {
            long gcd_ab = GCD(a, b);
            return ((a / gcd_ab) * (b / gcd_ab)) * gcd_ab;
        }
    }
}
