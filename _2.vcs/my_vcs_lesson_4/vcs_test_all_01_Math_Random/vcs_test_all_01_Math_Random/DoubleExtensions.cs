using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace vcs_test_all_01_Math_Random
{
    static class DoubleExtensions
    {
        // Convert a double into words. 
        // E.g. "one thousand eight hundred twelve."
        public static string ToWords(this double num)
        {
            // Return a word representation of the whole number value.
            // Remove any fractional part.
            num = Math.Truncate(num);

            // If the number is 0, return zero.
            if (num == 0) return "zero";

            string[] groups = {"", "thousand", "million", "billion", "trillion", "quadrillion", "?", "??", "???", "????"};
            string result = "";

            // Process the groups, smallest first.
            int group_num = 0;
            while (num > 0)
            {
                // Get the next group of three digits.
                double quotient = Math.Truncate(num / 1000);
                int remainder = (int)Math.Round(num - quotient * 1000);
                num = quotient;

                // Convert the group into words.
                if (remainder != 0)
                    result = GroupToWords(remainder) +
                        " " + groups[group_num] + ", " +
                        result;

                // Get ready for the next group.
                group_num++;
            }

            // Remove the trailing ", ".
            if (result.EndsWith(", "))
                result = result.Substring(0, result.Length - 2);

            return result.Trim();
        }

        // Convert a number between 0 and 999 into words.
        private static string GroupToWords(int num)
        {
            string[] one_to_nineteen = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eightteen", "nineteen"};
            string[] multiples_of_ten = {"twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"};

            // If the number is 0, return an empty string.
            if (num == 0) return "";

            // Handle the hundreds digit.
            int digit;
            string result = "";
            if (num > 99)
            {
                digit = (int)(num / 100);
                num = num % 100;
                result = one_to_nineteen[digit] + " hundred";
            }

            // If num = 0, we have hundreds only.
            if (num == 0) return result.Trim();

            // See if the rest is less than 20.
            if (num < 20)
            {
                // Look up the correct name.
                result += " " + one_to_nineteen[num];
            }
            else
            {
                // Handle the tens digit.
                digit = (int)(num / 10);
                num = num % 10;
                result += " " + multiples_of_ten[digit - 2];

                // Handle the final digit.
                if (num > 0)
                    result += " " + one_to_nineteen[num];
            }

            return result.Trim();
        }
    }
}
