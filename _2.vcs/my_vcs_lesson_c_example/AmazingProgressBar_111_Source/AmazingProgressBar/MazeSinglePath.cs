using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Text;

namespace GAW
{
    partial class AmazingProgressBar
    {
		/// <summary>
		/// 	Static class to generate a simple maze with a (mostly) single path.
		/// </summary>
		public static class MazeSinglePath
		{
            /// <summary>
            /// 	Generate a single path maze using the system default random number generator.
            /// </summary>
			/// <param name="rows">Number of rows.</param>
			/// <param name="cols">Number of columns.</param>
            /// <param name="direction">Primary direction of maze flow.</param>
			/// <returns>Generated maze.</returns>
			public static Maze Generate(int rows, int cols, Maze.Dir direction)
			{
				return Generate(rows, cols, direction, new Random());
			}

			/// <summary>
            /// 	Generate a single path maze using the given seed for the random number generator.
			/// </summary>
			/// <param name="rows">Number of rows.</param>
			/// <param name="cols">Number of columns.</param>
            /// <param name="direction">Primary direction of maze flow.</param>
			/// <param name="randomSeed">Seed for random number generator.</param>
			/// <returns>Generated maze.</returns>
			public static Maze Generate(int rows, int cols, Maze.Dir direction, int randomSeed)
			{
				return Generate(rows, cols, direction, new Random(randomSeed));
			}

			/// <summary>
            /// 	Generate a single path maze.
			/// </summary>
			/// <param name="rows">Number of rows.</param>
			/// <param name="cols">Number of columns.</param>
            /// <param name="direction">Primary direction of maze flow.</param>
			/// <param name="random">Random number generator.</param>
			/// <returns>Generated maze.</returns>
			public static Maze Generate(int rows, int cols, Maze.Dir direction, Random random)
			{
				Maze.Cell firstCell;
				Maze.Cell lastCell;

				Maze.Dir[,] map = SimpleMap.Generate(rows, cols, direction, random, out firstCell, out lastCell);
				Maze maze = new Maze(map, firstCell);
				return maze;
			}
		}
	}
}
