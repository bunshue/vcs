using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace vcs_test_all_01_Random
{
    public static class RandomizeStuff
    {
        // Randomize a 2D array.
        public static void Randomize2<T>(this T[,] random_array2D)
        {
            int ROW = random_array2D.GetUpperBound(0) + 1;  // 取得指定維度的上限，第0項就是橫列數 ROW
            int COL = random_array2D.GetUpperBound(1) + 1;  // 取得指定維度的上限，第1項就是直行數 COL
            int num_cells = ROW * COL;

            // Randomize the array.
            Random rand = new Random();
            for (int i = 0; i < num_cells - 1; i++)
            {
                // Pick a random cell between i and the end of the array.
                int j = rand.Next(i, num_cells);

                // Convert to row/column indexes.
                int row_i = i / COL;
                int col_i = i % COL;
                int row_j = j / COL;
                int col_j = j % COL;

                // Swap cells i and j.
                T temp = random_array2D[row_i, col_i];
                random_array2D[row_i, col_i] = random_array2D[row_j, col_j];
                random_array2D[row_j, col_j] = temp;
            }
        }
    }
}
