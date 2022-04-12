using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace vcs_test_all_01_Math
{
    public static class StringStuff
    {
        // Return the int's ordinal extension.
        public static string ToOrdinal(this int value)
        {
            // Start with the most common extension.
            string extension = "th";

            // Examine the last 2 digits.
            int last_digits = value % 100;

            // If the last digits are 11, 12, or 13, use th. Otherwise:
            if (last_digits < 11 || last_digits > 13)
            {
                // Check the last digit.
                switch (last_digits % 10)
                {
                    case 1:
                        extension = "st";
                        break;
                    case 2:
                        extension = "nd";
                        break;
                    case 3:
                        extension = "rd";
                        break;
                }
            }

            return extension;
        }
    }
}
