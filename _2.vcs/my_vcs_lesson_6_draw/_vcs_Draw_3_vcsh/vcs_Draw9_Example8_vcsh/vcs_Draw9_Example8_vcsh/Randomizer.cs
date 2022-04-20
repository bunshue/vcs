using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace vcs_Draw9_Example8_vcsh
{
    public static class Randomizer
    {
        // Used to randomize.
        private static Random Rand = new Random();

        // Randomize an array.
        public static void Randomize<T>(this T[] items)
        {
            // For each spot in the array, pick
            // a random item to swap into that spot.
            for (int i = 0; i < items.Length - 1; i++)
            {
                int j = Rand.Next(i, items.Length);
                T temp = items[i];
                items[i] = items[j];
                items[j] = temp;
            }
        }
    }
}
