using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace vcs_DrawB_Matrix
{
    public static class RandomizeStuff
    {
        // Randomize a 2D array.
        public static void Randomize<T>(this T[,] values)
        {
            // Get the dimensions.
            int num_rows = values.GetUpperBound(0) + 1;
            int num_cols = values.GetUpperBound(1) + 1;
            int num_cells = num_rows * num_cols;

            // Randomize the array.
            Random rand = new Random();
            for (int i = 0; i < num_cells - 1; i++)
            {
                // Pick a random cell between i and the end of the array.
                int j = rand.Next(i, num_cells);

                // Convert to row/column indexes.
                int row_i = i / num_cols;
                int col_i = i % num_cols;
                int row_j = j / num_cols;
                int col_j = j % num_cols;

                // Swap cells i and j.
                T temp = values[row_i, col_i];
                values[row_i, col_i] = values[row_j, col_j];
                values[row_j, col_j] = temp;
            }
        }
    }
}
