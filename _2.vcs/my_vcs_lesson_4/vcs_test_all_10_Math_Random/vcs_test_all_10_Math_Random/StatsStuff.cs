using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace vcs_test_all_10_Math_Random
{
    public static class StatsStuff
    {
        // Return the standard deviation of an array of Doubles.
        //
        // If the second argument is True, evaluate as a sample.
        // If the second argument is False, evaluate as a population.
        public static double StdDev<T>(this IEnumerable<T> values, bool as_sample)
        {
            // Convert into an enumerable of doubles.
            IEnumerable<double> doubles =
                values.Select(value => Convert.ToDouble(value));

            // Get the mean.
            double mean = doubles.Sum() / doubles.Count();

            // Get the sum of the squares of the differences
            // between the values and the mean.
            var squares_query =
                from double value in doubles
                select (value - mean) * (value - mean);
            double sum_of_squares = squares_query.Sum();

            if (as_sample)
            {
                return Math.Sqrt(sum_of_squares / (doubles.Count() - 1));
            }
            else
            {
                return Math.Sqrt(sum_of_squares / doubles.Count());
            }
        }
    }
}
