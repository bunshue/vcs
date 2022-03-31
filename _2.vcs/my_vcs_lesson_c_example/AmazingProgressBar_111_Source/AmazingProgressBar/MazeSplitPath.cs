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
		/// 	Static class to generate a simple map maze but using converging or diverging paths.
		/// </summary>
		public static class MazeSplitPath
		{
	        /// <summary>
	        /// 	Type of maze path.
	        /// </summary>
			public enum PathType
			{
			    /// <summary>
				/// 	Start at East and West ends, converging in the middle.
			    /// </summary>
				ConvergeEW,
				
				/// <summary>
				/// 	Start at North and South ends, converging in the middle.
				/// </summary>
				ConvergeNS,
				
				/// <summary>
				/// 	Start in the middle, ending in the East and West ends.
				/// </summary>
				DivergeEW,
				
				/// <summary>
				/// 	Start in the middle, ending in the North and South ends.
				/// </summary>
				DivergeNS
			};

            /// <summary>
            /// 	Generate a split path maze using the system default random number generator.
            /// </summary>
			/// <param name="rows">Number of rows.</param>
			/// <param name="cols">Number of columns.</param>
            /// <param name="pathType">Type of maze path.</param>
			/// <returns>Generated maze.</returns>
			public static Maze Generate(int rows, int cols, PathType pathType)
			{
				return Generate(rows, cols, pathType, new Random());
			}

			/// <summary>
            /// 	Generate a split path maze using the given seed for the random number generator.
			/// </summary>
			/// <param name="rows">Number of rows.</param>
			/// <param name="cols">Number of columns.</param>
            /// <param name="pathType">Type of maze path.</param>
			/// <param name="randomSeed">Seed for random number generator.</param>
			/// <returns>Generated maze.</returns>
			public static Maze Generate(int rows, int cols, PathType pathType, int randomSeed)
			{
				return Generate(rows, cols, pathType, new Random(randomSeed));
			}

			/// <summary>
            /// 	Generate a split path maze.
			/// </summary>
			/// <param name="rows">Number of rows.</param>
			/// <param name="cols">Number of columns.</param>
            /// <param name="pathType">Type of maze path.</param>
			/// <param name="random">Random number generator.</param>
			/// <returns>Generated maze.</returns>
			public static Maze Generate(int rows, int cols, PathType pathType, Random random)
			{
				// If pathType is EW, randomly pick an E/W direction
				// Correspondingly, if pathType is NS, randomly pick a N/S direction.
				Maze.Dir direction;
				int rnd = random.Next(2);
				if (pathType == PathType.ConvergeEW || pathType == PathType.DivergeEW)
				{
                    direction = (rnd == 0) ? Maze.Dir.E : Maze.Dir.W;
				}
				else
				{
                    direction = (rnd == 0) ? Maze.Dir.N : Maze.Dir.S;
				}

				Maze.Cell firstCell;
				Maze.Cell lastCell;
				Maze.Dir[,] map = SimpleMap.Generate(rows, cols, direction, random, out firstCell, out lastCell);

				Maze.Cell[] startCells;
				if (pathType == PathType.DivergeEW || pathType == PathType.DivergeNS)
				{
					startCells = new Maze.Cell[1];
					startCells[0] = new Maze.Cell(rows / 2, cols / 2);
				}
				else
				{
					startCells = new Maze.Cell[2];
					startCells[0] = firstCell;
					startCells[1] = lastCell;
				}

				Maze maze = new Maze(map, startCells);
				return maze;
			}
		}
	}
}
