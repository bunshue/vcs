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
		/// 	Static class to generate a simple map.
		/// </summary>
		/// <remarks>
		/// 	Refer to the <c>Maze</c> class for a discussion of maps, paths, and mazes.
		/// </remarks>
		public static class SimpleMap
		{
		    /// <summary>
            /// 	Generate a single map using the system default random number generator.
		    /// </summary>
			/// <param name="rows">Number of rows.</param>
			/// <param name="cols">Number of columns.</param>
            /// <param name="direction">Primary direction of map flow.</param>
		    /// <param name="firstCell">Cell where map generation began.</param>
		    /// <param name="lastCell">Cell where map generation ended.</param>
			/// <returns>Generated map.</returns>
			public static Maze.Dir[,] Generate(int rows, int cols, Maze.Dir direction,
									  		   out Maze.Cell firstCell, out Maze.Cell lastCell)
			{
				return Generate(rows, cols, direction, new Random(), out firstCell, out lastCell);
			}

			/// <summary>
            /// 	Generate a simple map using the given seed for the random number generator.
			/// </summary>
			/// <param name="rows">Number of rows.</param>
			/// <param name="cols">Number of columns.</param>
            /// <param name="direction">Primary direction of map flow.</param>
			/// <param name="randomSeed">Seed for random number generator.</param>
		    /// <param name="firstCell">Cell where map generation began.</param>
		    /// <param name="lastCell">Cell where map generation ended.</param>
			/// <returns>Generated map.</returns>
			public static Maze.Dir[,] Generate(int rows, int cols, Maze.Dir direction, int randomSeed,
									  		   out Maze.Cell firstCell, out Maze.Cell lastCell)
			{
				return Generate(rows, cols, direction, new Random(randomSeed), out firstCell, out lastCell);
			}

			/// <summary>
            /// 	Generate a simple map.
			/// </summary>
			/// <param name="rows">Number of rows.</param>
			/// <param name="cols">Number of columns.</param>
            /// <param name="direction">Primary direction of map flow.</param>
			/// <param name="random">Random number generator.</param>
		    /// <param name="firstCell">Cell where map generation began.</param>
		    /// <param name="lastCell">Cell where map generation ended.</param>
			/// <returns>Generated map.</returns>
			public static Maze.Dir[,] Generate(int rows, int cols, Maze.Dir direction, Random random,
									  		   out Maze.Cell firstCell, out Maze.Cell lastCell)
			{
				firstCell = null;
				lastCell = null;

				if (rows < 1)
				{
					throw new ArgumentException("rows");
				}
				if (cols < 1)
				{
					throw new ArgumentException("cols");
				}
				if (random == null)
				{
					throw new ArgumentNullException("random");
				}

				int maxRow = rows - 1;
				int maxCol = cols - 1;
				Maze.Dir[,] map = new Maze.Dir[rows, cols];

				for (int r = 0; r < rows; r++)
				{
					for (int c = 0; c < cols; c++)
					{
						map[r,c] = Maze.Dir.None;
					}
				}

				// Following are the rules for generating a simple map.
				//
				// The directions are F(orward), B(ackward) and S(ideways).
				// What they actually are depends on the direction parameter.
				// For example, if direction == Right, then forward is East, backward is West,
				// and sideways is north or south.
				//
				// Start at one of the most backward corner cells.  Until stuck, use the following rules (in order) to determine
				// the next cell:
				// 1. If can only go in one direction, go in that direction.
				// 2. If we can go backward, go backward.
				// 3. If there is only one empty cell in a sideways direction, go in that direction,
				// 4. If more than one empty cell in both of the sideways directions, randomly pick one of those directions
				// 5. Pick a random direction from the ones available; but only allowed to go forward if
				//      (a) at a sideways edge, and
				//      (b) more than two steps from the forward most end, and
				//      (c) back most filled column is not more than three steps backward

                Maze.Dir dirFor = direction;
                Maze.Dir dirBack = Maze.Opposite(direction);
                Maze.Dir dirSide1 = Maze.Dir.None;
                Maze.Dir dirSide2 = Maze.Dir.None;

				int startRow = -1;
				int startCol = -1;
				int rnd = random.Next(2);

				int backSize = 0;
				int backVal = 0;

				switch (direction)
				{
                    case Maze.Dir.E : dirSide1 = Maze.Dir.N; dirSide2 = Maze.Dir.S;
                    				  startRow = (rnd == 0) ? 0 : maxRow;
					                  startCol = 0;
									  backSize = rows;
									  backVal = -1;
									  break;

                    case Maze.Dir.W : dirSide1 = Maze.Dir.N; dirSide2 = Maze.Dir.S;
					                  startRow = (rnd == 0) ? 0 : maxRow;
					                  startCol = maxCol;
									  backSize = rows;
									  backVal = cols;
									  break;

                    case Maze.Dir.N : dirSide1 = Maze.Dir.E; dirSide2 = Maze.Dir.W;
					                  startRow = maxRow;
					                  startCol = (rnd == 0) ? 0 : maxCol;
									  backSize = cols;
									  backVal = -1;
									  break;

                    case Maze.Dir.S : dirSide1 = Maze.Dir.E; dirSide2 = Maze.Dir.W;
					                  startRow = 0;
					                  startCol = (rnd == 0) ? 0 : maxCol;
									  backSize = cols;
									  backVal = rows;
									  break;
				}

				// Use this array to track rows/cols which are falling behind
				int[] backMost = new int[backSize];
				for (int b = 0; b < backSize; b++)
				{
					backMost[b] = backVal;
				}

				// Starting cell
                firstCell = new Maze.Cell(startRow, startCol);
				Maze.Cell cur = new Maze.Cell(startRow, startCol);
				int emptyCells = rows * cols - 1;

				// Keep going until we get stuck
				while (true)
				{
					// Update backMost array
					switch (direction)
					{
						case Maze.Dir.E : backMost[cur.Row] = Math.Max(backMost[cur.Row], cur.Col); break;
						case Maze.Dir.W : backMost[cur.Row] = Math.Min(backMost[cur.Row], cur.Col); break;
						case Maze.Dir.N : backMost[cur.Col] = Math.Max(backMost[cur.Col], cur.Row); break;
						case Maze.Dir.S : backMost[cur.Col] = Math.Min(backMost[cur.Col], cur.Row); break;
					}

					Maze.Dir dir = Maze.Dir.None;

					// Count # of steps that can be travelled in each the directions
					// If 2 or more steps, just list as 2
					int numFor   = CountCanGo(map, cur, dirFor);
					int numBack  = CountCanGo(map, cur, dirBack);
					int numSide1 = CountCanGo(map, cur, dirSide1);
					int numSide2 = CountCanGo(map, cur, dirSide2);

					// 1. If can only go one direction, then dude, that is the direction we go
					if (numFor > 0 && (numBack + numSide1 + numSide2 == 0))
					{
						dir = dirFor;
						goto DirDecided;
					}
					if (numBack > 0 && (numFor + numSide1 + numSide2 == 0))
					{
						dir = dirBack;
						goto DirDecided;
					}
					if (numSide1 > 0 && (numFor + numBack + numSide2 == 0))
					{
						dir = dirSide1;
						goto DirDecided;
					}
					if (numSide2 > 0 && (numFor + numBack + numSide1 == 0))
					{
						dir = dirSide2;
						goto DirDecided;
					}

					// 2. If we can go back - that is the ONLY direction to go
					if (numBack > 0)
					{
						dir = dirBack;
						goto DirDecided;
					}

					// 3. If can only go one step sideways, then go sideways
					if (numSide1 == 1)
					{
						dir = dirSide1;
						goto DirDecided;
					}
					if (numSide2 == 1)
					{
						dir = dirSide2;
						goto DirDecided;
					}

					// 4. If can go more than one step in both sideways directions, randomly pick one of the two
					if (numSide1 > 1 && numSide2 > 1)
					{
						rnd = random.Next(2);
						dir = (rnd == 0) ? dirSide1 : dirSide2;
						goto DirDecided;
					}

					// 5. Pick a random direction from the ones available; but only allowed to go east if
					//      (a) at sideways edge
					//      (b) more than two steps from the forwards end, and
					//      (c) back most filled cells not more than three steps behind
					List<Maze.Dir> dirList = new List<Maze.Dir>();
					if (numSide1 > 0)
					{
						dirList.Add(dirSide1);
					}
					if (numSide2 > 0)
					{
						dirList.Add(dirSide2);
					}
					if (numFor > 0)
					{
						bool backMostOk = false;
						bool farFromForEdge = false;
						bool onSideEdge = false;

						switch (direction)
						{
							case Maze.Dir.E : 
							{
								int backMostCol = cols;
								for (int r = 0; r < rows; r++)
								{
									backMostCol = Math.Min(backMostCol, backMost[r]);
								}
								backMostOk = (backMostCol >= cur.Col - 3);
								farFromForEdge = (cur.Col < maxCol - 2);
								onSideEdge = (cur.Row == 0 || cur.Row == maxRow);
								break;
							}
							case Maze.Dir.W : 
							{
								int backMostCol = -1;
								for (int r = 0; r < rows; r++)
								{
									backMostCol = Math.Max(backMostCol, backMost[r]);
								}
								backMostOk = (backMostCol <= cur.Col + 3);
								farFromForEdge = (cur.Col > 2);
								onSideEdge = (cur.Row == 0 || cur.Row == maxRow);
								break;
							}
							case Maze.Dir.N : 
							{
								int backMostRow = rows;
								for (int c = 0; c < cols; c++)
								{
									backMostRow = Math.Min(backMostRow, backMost[c]);
								}
								backMostOk = (backMostRow >= cur.Row - 3);
								farFromForEdge = (cur.Row < maxRow - 2);
								onSideEdge = (cur.Col == 0 || cur.Col == maxCol);
								break;
							}
							case Maze.Dir.S : 
							{
								int backMostRow = -1;
								for (int c = 0; c < cols; c++)
								{
									backMostRow = Math.Max(backMostRow, backMost[c]);
								}
								backMostOk = (backMostRow <= cur.Row + 3);
								farFromForEdge = (cur.Row > 2);
								onSideEdge = (cur.Col == 0 || cur.Col == maxCol);
								break;
							}
						}

						if (backMostOk && farFromForEdge && onSideEdge)
						{
							dirList.Add(dirFor);
						}
					}

					// If dirList is empty, then we've reached a deadend, and must quit...
					if (dirList.Count == 0)
					{
						break;
					}

					// Otherwise, pick a dir
					rnd = random.Next(dirList.Count);
					dir = dirList[rnd];

DirDecided:
					// Update map
					Maze.Cell nxt = new Maze.Cell(cur, dir);
                    lastCell = nxt;

					map[cur.Row, cur.Col] |= dir;
					map[nxt.Row, nxt.Col] |= Maze.Opposite(dir);
					emptyCells--;
					cur = nxt;
				}

				// If still have empty cells, then cycle through and join the empty cell to one
				// of it's non-empty neighbours (randomly) chosen.
				//
				// Cycle throught the cells east-to-west.  For each, randomly join to a finished cell
				// in an north, south or west direction.  Only pick east if that is the only option.
				// This is to maintain a general sense of east-to-west motion.
				//
				// Keep track of empty cells with NO non-empty neighbours, and iterate through that
				// list next.  Keep looping till all empty cells are filled.

				if (emptyCells > 0)
				{
					List<Maze.Cell> empty = new List<Maze.Cell>();

					for (int col = 0; col < cols; col++)
					{
						for (int row = 0; row < rows; row++)
						{
							if (map[row, col] == Maze.Dir.None)
							{
								if (!RandomJoin(random, map, row, col))
								{
									empty.Add(new Maze.Cell(row, col));
								}
							}
						}
					}

					while (empty.Count > 0)
					{
	                    List<Maze.Cell> stillEmpty = new List<Maze.Cell>();
	                    foreach (Maze.Cell cell in empty)
						{
							if (!RandomJoin(random, map, cell.Row, cell.Col))
							{
								stillEmpty.Add(cell);
							}
						}
						empty = stillEmpty;
					}
				}

				return map;
			}

			private static bool RandomJoin(Random random, Maze.Dir[,] map, int row, int col)
			{
                int maxRow = map.GetLength(0) - 1;
                int maxCol = map.GetLength(1) - 1;
                
				List<Maze.Dir> dirList = new List<Maze.Dir>();

				if (col > 0 && map[row, col - 1] != Maze.Dir.None)
				{
					dirList.Add(Maze.Dir.W);
				}
				if (row > 0 && map[row - 1, col] != Maze.Dir.None)
				{
					dirList.Add(Maze.Dir.N);
				}
				if (row < maxRow && map[row + 1, col] != Maze.Dir.None)
				{
					dirList.Add(Maze.Dir.S);
				}

				if (dirList.Count == 0)
				{
					if (col < maxCol && map[row, col + 1] != Maze.Dir.None)
					{
						dirList.Add(Maze.Dir.E);
					}
				}

				if (dirList.Count == 0)
				{
					return false;
				}

				Maze.Dir dir = dirList[random.Next(dirList.Count)];
				Maze.Cell nn = new Maze.Cell(row, col, dir);

				map[row, col] |= dir;
				map[nn.Row, nn.Col] |= Maze.Opposite(dir);

				return true;
			}

			private static int CountCanGo(Maze.Dir[,] map, Maze.Cell cur, Maze.Dir dir)
			{
                int maxRow = map.GetLength(0) - 1;
                int maxCol = map.GetLength(1) - 1;
                
				switch (dir)
				{
					case Maze.Dir.N :
					{
						if (cur.Row > 0 && map[cur.Row - 1, cur.Col] == Maze.Dir.None)
						{
							if (cur.Row > 1 && map[cur.Row - 2, cur.Col] == Maze.Dir.None) return 2;
							return 1;
						}
						break;
					}

					case Maze.Dir.E :
					{
						if (cur.Col <  maxCol && map[cur.Row, cur.Col + 1] == Maze.Dir.None)
						{
							if (cur.Col < (maxCol - 1) && map[cur.Row, cur.Col + 2] == Maze.Dir.None) return 2;
							return 1;
						}
						break;
					}

					case Maze.Dir.S :
					{
						if (cur.Row <  maxRow && map[cur.Row + 1, cur.Col] == Maze.Dir.None)
						{
							if (cur.Row < (maxRow - 1) && map[cur.Row + 2, cur.Col] == Maze.Dir.None) return 2;
							return 1;
						}
						break;
					}

					case Maze.Dir.W :
					{
						if (cur.Col > 0 && map[cur.Row, cur.Col - 1] == Maze.Dir.None)
						{
							if (cur.Col > 1 && map[cur.Row, cur.Col - 2] == Maze.Dir.None) return 2;
							return 1;
						}
						break;
					}
				}
				return 0;
			}
		}
	}
}
