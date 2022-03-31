using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Text;

namespace GAW
{
    partial class AmazingProgressBar
    {
        /// <summary>
        /// 	Represesents a maze enclosed by a rectanglar area.
        /// </summary>
		/// <remarks>
		///		A maze is composed of a <c>map</c> and a <c>path</c>.
		/// 	The map defines the structure of the maze, that is, the location of all the walls.
		/// 	The path defines the order in which the maze is filled while used in a progress bar.
		///		For any given map, there are numerous possible paths.
		///		<para>
		/// 	Maze and map sizes are given as rows and columns.
		/// 	Row indexes are zero based starting at the top.
		/// 	Column indexes are zero based starting at the left.
		/// 	</para>
		/// </remarks>
		public class Maze
		{
			/// <summary>
			/// 	Movement direction flags.
			/// </summary>
			[Flags]
			public enum Dir
			{
				/// <summary>
				/// 	No movement.  Used to indicate an empty, or unassigned cell.
				/// </summary>
				None = 0x00,
				
				/// <summary>
				/// 	Can go north (up).
				/// </summary>
				N = 0x01,
				
				/// <summary>
				/// 	Can go east (right).
				/// </summary>
				E = 0x02,
				
				/// <summary>
				/// 	Can go south (down).
				/// </summary>
				S = 0x04,
				
				/// <summary>
				/// 	Can go west (left).
				/// </summary>
				W = 0x08,

				/// <summary>
				/// 	Mask representing all four direction (N, E, S, W).
				/// </summary>
				All = 0x0F,

				/// <summary>
				/// 	Mapped flag - used internally for generating paths.
				/// </summary>
				MAP = 0x80
			};

            /// <summary>
            /// 	Helper method to determine the opposite of a given direction.
            /// </summary>
            /// <param name="dir">Direction</param>
            /// <returns>Opposite direction</returns>
			public static Dir Opposite(Dir dir)
			{
				switch (dir)
				{
					case Dir.N: return Dir.S;
					case Dir.E: return Dir.W;
					case Dir.S: return Dir.N;
					case Dir.W: return Dir.E;
				}
				return Dir.None;
			}

            /// <summary>
            /// 	Represents the coordinates of a single cell in a maze.
            /// </summary>
			public class Cell
			{
			    /// <summary>
			    /// 	Copy constructor.
			    /// </summary>
			    /// <param name="cell">Cell to copy.</param>
				/// <exception cref="System.ArgumentNullException">
				///		Thrown if <c>cell</c> is null.
				/// </exception>
				public Cell(Cell cell)
				{
					if (cell == null)
					{
						throw new ArgumentNullException("cell");
					}
					Row = cell.Row;
					Col = cell.Col;
				}

				/// <summary>
				/// 	Constructor using given coordinates.
				/// </summary>
				/// <param name="row">Row coordinate</param>
				/// <param name="col">Column coordinate</param>
				public Cell(int row, int col)
				{
					Row = row;
					Col = col;
				}

				/// <summary>
				/// 	Constructor using coordinates of given cell after direction applied.
				/// 	Constucted object has coordinates of <c>cell</c> after movement of one step in direction <c>dir</c>.
				/// </summary>
				/// <param name="cell">Cell coordinate to copy.</param>
				/// <param name="dir">Direction to move.</param>
				public Cell(Cell cell, Dir dir) : this(cell.Row, cell.Col, dir)
				{ }

                /// <summary>
				/// 	Constructor using given coordinates after direction applied.
				/// 	Constucted object has coordinates of <c>row</c>, <c>col</c> after movement of one step in direction <c>dir</c>.
                /// </summary>
                /// <param name="row">Start row coordinate.</param>
                /// <param name="col">Start column coordinate.</param>
                /// <param name="dir">Direction to move.</param>
				public Cell(int row, int col, Dir dir)
				{
					switch (dir)
					{
						case Dir.N: Row = row - 1; Col = col;     break;
						case Dir.E: Row = row;     Col = col + 1; break;
						case Dir.S: Row = row + 1; Col = col;     break;
						case Dir.W: Row = row;     Col = col - 1; break;
						default:
						{
							throw new ArgumentException("dir not one of N,E,S,W");
						}
					}
				}

				/// <summary>
				/// 	Row in maze. The range is [0, number of rows - 1].
				/// 	Row zero is the top row.
				/// </summary>
				public readonly int Row;
				
				/// <summary>
				/// 	Column in maze. The range is [0, number of rows - 1].
				/// 	Column zero is the left column.
				/// </summary>
				public readonly int Col;

				/// <summary>
				/// 	String representation of cell.
				/// </summary>
				/// <returns>String.</returns>
				public override string ToString()
				{
					return string.Format("Cell R={0} C={1}");
				}

				/// <summary>
				/// 	Compares this Cell with another object.
				/// </summary>
				/// <param name="o">Other object.</param>
				/// <returns><c>True</c> if <c>o</c> is not null, is a <c>Cell</c>, and has the same coordinate as <c>this</c>. <c>False</c> otherwise.</returns>
				public override bool Equals(object o)
				{
					if (o == null)
					{
						return false;
					}
					Cell co = o as Cell;
					if ((object)co == null)
					{
						return false;
					}
					return (co.Row == Row) && (co.Col == Col);
				}

				/// <summary>
				/// 	Calculates hashcode for this object.
				/// </summary>
				/// <returns>Hashcode.</returns>
				public override int GetHashCode()
				{
					return Row ^ Col;
				}
			}

			/// <summary>
			/// 	Constructor using two-dimensional array of <c>Dir</c> values, and starting coordinates.
			/// </summary>
			/// <param name="map">Valid movement directions for each cell; first dimension is row index; second dimension is column index.</param>
			/// <param name="startRow">Row coordinate of starting cell.</param>
			/// <param name="startCol">Column coordinate of starting cell.</param>
			public Maze(Dir[,] map, int startRow, int startCol)	: this(map, new Cell(startRow, startCol))
			{ }

            /// <summary>
            /// 	Constructor using 2D array of <c>Dir</c> values, and starting cell.
            /// </summary>
			/// <param name="map">Valid movement directions for each cell; first dimension is row index; second dimension is column index.</param>
            /// <param name="startCell">Starting cell.</param>
            public Maze(Dir[,] map, Cell startCell) : this(map, new Cell[1] { startCell })
            { }

			/// <summary>
            /// 	Constructor using 2D array of <c>Dir</c> values, and list of starting cells.
			/// </summary>
			/// <param name="map">Valid movement directions for each cell; first dimension is row index; second dimension is column index.</param>
            /// <param name="startCells">List of starting cells.</param>
			/// <exception cref="System.ArgumentNullException">
			///		Thrown if <c>map</c> or <c>startCells</c> is null.
			/// </exception>
			/// <exception cref="System.ArgumentNullException">
			///		Thrown if either dimension of <c>map</c> is less than one, length of <c>startCells</c> is less than one,
			/// 	or <c>startCells</c> contains any invalid or repeating cells.
			/// </exception>
			public Maze(Dir[,] map, Cell[] startCells)
			{
				if (map == null)
				{
					throw new ArgumentNullException("map");
				}
				if (map.GetLength(0) == 0 || map.GetLength(1) == 0)
				{
					throw new ArgumentException("map has a zero length dimension");
				}
				if (startCells == null)
				{
					throw new ArgumentNullException("startCells");
				}
				if (startCells.Length == 0)
				{
					throw new ArgumentException("startCells.Length is zero; must be 1+");
				}

				Map = map;

				// Turn off all non-NSEW flags
				for (int r = 0; r < Rows; r++)
				{
					for (int c = 0; c < Cols; c++)
					{
						Map[r,c] &= Dir.All;
					}
				}

				Paths = GeneratePaths(startCells);
			}

			/// <summary>
			/// 	Map of the maze.
			/// 	<para>
			/// 	Each entry represents one cell in the maze, with the values
			/// 	indicating the direction(s) one can move from that cell.
			/// 	The first dimension is the rows.  The second dimenion is columns.
			/// 	</para>
			/// 	<para>
			/// 	For example, from cell with the value <c>Dir.N | Dir.E</c>, one
			/// 	could move north or east, but not south or west.
			/// 	</para>
			/// </summary>
			public readonly Dir[,] Map;
			
			/// <summary>
			/// 	Paths through the maze.
			/// 	<para>
			/// 	The first dimension is the number of steps from the nearest starting cell.
			/// 	The second dimension are all the cells at that distance.
			/// 	Each reachable cell occurs once and only once in this array.
			/// 	</para>
			/// 	<para>
			/// 	For example, <c>Paths[0]</c> is the list of start cells specified in the constructor,
			/// 	and <c>Paths[1}</c> is the list of a cells one step from a start cell.
			/// 	</para>
			/// </summary>
			public readonly Cell[][] Paths;

			/// <summary>
			/// 	Number of rows in the maze (1+).
			/// </summary>
			public int Rows
			{
				get { return Map.GetLength(0); }
			}

			/// <summary>
			/// 	Number of columns in the maze (1+).
			/// </summary>
			public int Cols
			{
				get { return Map.GetLength(1); }
			}

			/// <summary>
			/// 	Test if a cell is valid.
			/// </summary>
			/// <param name="cell">Cell to test.</param>
			/// <returns><c>True</c> if <c>cell</c> is not <c>null</c> and whose coordinates are within this maze, <c>false</c> otherwise.</returns>
			public bool Valid(Cell cell)
			{
				if (cell == null)
				{
					return false;
				}
				return Valid(cell.Row, cell.Col);
			}

			/// <summary>
			/// 	Test if coordinates are within this maze.
			/// </summary>
			/// <param name="row">Row coordinate.</param>
			/// <param name="col">Column coordinate.</param>
			/// <returns><c>True</c> if the coordinates are within this maze, <c>false</c> otherwise.</returns>
			public bool Valid(int row, int col)
			{
				return (row >= 0) && (row < Rows) && (col >= 0) && (col < Cols);
			}

			private Cell[][] GeneratePaths(Cell[] startCells)
			{
				// Make sure all startCells entries are unique
				for (int c = 0; c < startCells.Length; c++)
				{
					if (!Valid(startCells[c]))
					{
						throw new ArgumentException(string.Format("startCells entry [{0}] invalid cell", c));
					}
					for (int cc = c + 1; cc < startCells.Length; cc++)
					{
						if (startCells[c].Equals(startCells[cc]))
						{
							throw new ArgumentException(string.Format("startCells entries [{0}] and [{1}] are equivalent", c, cc));
						}
					}
				}

				// Build path array
				// The 1st rank is the progress bar step count, or distance from the nearest starting cell.
				// The 2nd rank is the number of cells at that step.
				//
				// As each cells is assigned to the path, set the MAP bit to prevent returning to a cell twice.

	            List<Maze.Cell[]> paths = new List<Maze.Cell[]>();
				List<Cell> curCells = new List<Cell>();

				// Add first cells
				for (int i = 0; i < startCells.Length; i++)
				{
					curCells.Add(new Cell(startCells[i]));
					Map[startCells[i].Row, startCells[i].Col] |= Dir.MAP;
				}
				paths.Add(curCells.ToArray());

				Dir[] map = new Dir[] { Dir.N, Dir.E, Dir.S, Dir.W };

				// Keep looping until curCells list is empty
				while (curCells.Count > 0)
				{
					List<Cell> newCurCells = new List<Cell>();

					// For each curCell, check all possible directions, and if can go that
					// direction, and the cell is not MAPped, then add that cell to the next cur list.
					foreach (Cell curCell in curCells)
					{
						foreach (Dir dir in map)
						{
							if ((Map[curCell.Row, curCell.Col] & dir) == dir)
							{
								Maze.Cell newCell = new Maze.Cell(curCell, dir);
								if ((Map[newCell.Row, newCell.Col] & Dir.MAP) != Dir.MAP)
								{
									Map[newCell.Row, newCell.Col] |= Dir.MAP;
									newCurCells.Add(newCell);
								}
							}
						}
					}
                    paths.Add(newCurCells.ToArray());

					curCells = newCurCells;
				}

				return paths.ToArray();
			}
		}
	}
}
