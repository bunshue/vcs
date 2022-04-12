using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace vcs_test_all_01_Math
{
    public static class PairsTools
    {
        public struct Pair<T>
        {
            // Values.
            public T Value1, Value2;

            // Constructor.
            public Pair(T value1, T value2)
            {
                Value1 = value1;
                Value2 = value2;
            }

            // Default ToString method.
            public override string ToString()
            {
                return Value1.ToString() + ", " + Value2.ToString();
            }
        }

        // Return a list of unique unordered pairs of items taken from an array.
        public static List<Pair<T>> Pairs<T>(this T[] items)
        {
            List<Pair<T>> results = new List<Pair<T>>();
            for (int i = 0; i < items.Length - 1; i++)
                for (int j = i + 1; j < items.Length; j++)
                    results.Add(new Pair<T>(items[i], items[j]));
            return results;
        }

        // Return a list of unique unordered pairs of items taken from an IEnumerable.
        public static List<Pair<T>> Pairs<T>(this IEnumerable<T> items)
        {
            return items.ToArray().Pairs();
        }
    }
}
