using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Text;

namespace GAW
{
	public static class MazeGenerator
	{
		public enum PathType { SinglePath, FasterPath, ZippyPath }

		private static int maxRow = 0;
		private static int maxCol = 0;
		private static Random random = null;

		private static Maze.Dir[,] dirs = null;

		public static Maze Generate(int rows, int cols, PathType pathType)
		{
			return Generate(rows, cols, new Random());
		}

		public static Maze Generate(int rows, int cols, int randomSeed, PathType pathType)
		{
			return Generate(rows, cols, new Random(randomSeed));
		}

		public static Maze Generate(int rows, int cols, Random random, PathType pathType)
		{
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

			maxRow = rows - 1;
			maxCol = cols - 1;
			dirs = new Maze.Dir[rows, cols];

			for (int r = 0; r < rows; r++)
			{
				for (int c = 0; c < cols; c++)
				{
					dirs[r,c] = Maze.Dir.None;
				}
			}

			// Ok, the rules for generating a maze are kinda fuzzy.  Here is my best attempt at an explanation.
			//
			// All maze generation assumes an east-to-west pathway.
			//
			// SinglePath
			// ----------
			// Start at either the NE or SE cell.  Until stuck, use the following rules (in order) to determine
			// the next cell:
			// 1. If can only go in one direction, go in that direction.
			// 2. If we can go west, go west.
			// 3. If there is only one empty cell to the north, go north.
			// 4. If there is only one empty cell to the south, go south.
			// 5. If more than one empty cell in both the north and south directions, randomly pick one of those directions
			// 6. Pick a random direction from the ones available; but only allowed to go east if
			//      (a) top or bottom row, and
			//      (b) more than two steps from the east end, and
			//      (c) west most filled column is not more than two steps west

			// Use this array to track the eastern most cell for each row
			int[] eastMostCols = new int[rows];
			for (int r = 0; r < rows; r++)
			{
				eastMostCols[r] = -1;
			}

			// Start at one of the corners in first column
			int startRow = (random.Next(2) == 0) ? 0 : maxRow;
			int startCol = 0;
			Maze.Cell cur = new Maze.Cell(startRow, startCol);
			int emptyCells = rows * cols - 1;

			// Keep going until we get stuck
			while (true)
			{
				// Update eastMostCols array
				eastMostCols[cur.Row] = Math.Max(eastMostCols[cur.Row], cur.Col);

				Maze.Dir dir = Maze.Dir.None;

				// Count # of steps that can be travelled in each of N/S/E directions
				// If 2 or more steps, just list as 2
				int numN = 0;
				if (cur.Row > 0 && dirs[cur.Row - 1, cur.Col] == Maze.Dir.None)
				{
					numN++;
					if (cur.Row > 1 && dirs[cur.Row - 2, cur.Col] == Maze.Dir.None)
					{
						numN++;
					}
				}

				int numE = 0;
				if (cur.Col <  maxCol && dirs[cur.Row, cur.Col + 1] == Maze.Dir.None)
				{
					numE++;
					if (cur.Col < (maxCol - 1) && dirs[cur.Row, cur.Col + 2] == Maze.Dir.None)
					{
						numE++;
					}
				}

				int numS = 0;
				if (cur.Row <  maxRow      && dirs[cur.Row + 1, cur.Col] == Maze.Dir.None)
				{
					numS++;
					if (cur.Row < (maxRow - 1) && dirs[cur.Row + 2, cur.Col] == Maze.Dir.None)
					{
						numS++;
					}
				}

				int numW = 0;
				if (cur.Col > 0 && dirs[cur.Row, cur.Col - 1] == Maze.Dir.None)
				{
					numW++;
					if (cur.Col > 1 && dirs[cur.Row, cur.Col - 2] == Maze.Dir.None)
					{
						numW++;
					}
				}

				// 1. If can only go one direction, then dude, that is the direction we go
				if (numN > 0 && (numE + numS + numW == 0))
				{
					dir = Maze.Dir.N;
					goto DirDecided;
				}
				if (numE > 0 && (numN + numS + numW == 0))
				{
					dir = Maze.Dir.E;
					goto DirDecided;
				}
				if (numS > 0 && (numN + numE + numW == 0))
				{
					dir = Maze.Dir.S;
					goto DirDecided;
				}
				if (numW > 0 && (numN + numE + numS == 0))
				{
					dir = Maze.Dir.W;
					goto DirDecided;
				}

				// 2. If we can go west - that is the ONLY direction to go
				if (cur.Col != 0 && dirs[cur.Row, cur.Col - 1] == Maze.Dir.None)
				{
					dir = Maze.Dir.W;
					goto DirDecided;
				}

				// 3. If can only go one step north, then go north
				if (numN == 1)
				{
					dir = Maze.Dir.N;
					goto DirDecided;
				}

				// 4. If can only go one step south, then go south
				if (numS == 1)
				{
					dir = Maze.Dir.S;
					goto DirDecided;
				}

				// 5. If can go more than one step north and more than step south, randomly pick one of the two
				if (numS > 1 && numN > 1)
				{
					dir = (random.Next(2) == 1) ? Maze.Dir.N : Maze.Dir.S;
					goto DirDecided;
				}

				// 6. Pick a random direction from the ones available; but only allowed to go east if
				//      (a) top or bottom row, and
				//      (b) more than two steps from the east end, and
				//      (c) west most filled column is not more than two steps west
				List<Maze.Dir> dirList = new List<Maze.Dir>();
				if (numN > 0)
				{
					dirList.Add(Maze.Dir.N);
				}
				if (numS > 0)
				{
					dirList.Add(Maze.Dir.S);
				}
				if (numE > 0)
				{
					int westMostCol = maxCol + 1;
					for (int r = 0; r < rows; r++)
					{
						westMostCol = Math.Min(westMostCol, eastMostCols[r]);
					}
					if (   (cur.Row == 0 || cur.Row == maxRow)
						&& (cur.Col < maxCol - 2)
						&& (westMostCol > cur.Col - 2))
					{
						dirList.Add(Maze.Dir.E);
					}
				}

				// If dirList is empty, then we've reached a deadend, and must quit...
				if (dirList.Count == 0)
				{
					break;
				}

				// Otherwise, pick a dir
				dir = dirList[random.Next(dirList.Count)];

DirDecided:
				// Update maze
				Maze.Cell nxt = new Maze.Cell(cur, dir);

				dirs[cur.Row, cur.Col] |= dir;
				dirs[nxt.Row, nxt.Col] |= Maze.Opposite(dir);
				emptyCells--;
				cur = nxt;
			}

			// If still have empty cells, then cycle through and join the empty cell to one
			// of it's non-empty neighbours (randomly) chosen.
			//
			// Keep track of empty cells with NO non-empty neighbours, and iterate through that
			// list next.  Keep looping till all empty cells are filled.

			if (emptyCells > 0)
			{
				List<Cell> empty = new List<Cell>();

				for (int row = 0; row < rows; row++)
				{
					for (int col = 0; col < cols; col++)
					{
						if (dirs[row, col] == Maze.Dir.None)
						{
							if (!RandomJoin(row, col))
							{
								empty.Add(new Cell(row, col));
							}
						}
					}
				}

				while (empty.Count > 0)
				{
					List<Cell> stillEmpty = new List<Cell>();
					foreach (Cell cell in empty)
					{
						if (!RandomJoin(cell.Row, cell.Col))
						{
							stillEmpty.Add(cell);
						}
					}
					empty = stillEmpty;
				}
			}

			// Build path array
			// The 1st rank is the progress bar step count, where the length is the length of the longest path.
			// The 2nd rank is the number of cells at that step.
			//
			// Use "walkers" to find the paths through the maze.  Start with one, and create another each time
			// there is a branch in the maze, and destroy when there is a deadend.

			List<Cell[]> path = new List<Cell[]>();

			// Add first cell to start
			Cell[] startCells = new Cell[1];
			Cell startCell = new Cell(startRow, startCol);
			startCells[0] = startCell;
			path.Add(startCells);

			// Create a walker for each cell connected to startCell
			List<Walker> walkers = new List<Walker>();
			if ((dirs[startRow, startCol] & Maze.Dir.N) == Maze.Dir.N) walkers.Add(new Walker(startCell, new Cell(startCell, Maze.Dir.N)));
			if ((dirs[startRow, startCol] & Maze.Dir.E) == Maze.Dir.E) walkers.Add(new Walker(startCell, new Cell(startCell, Maze.Dir.E)));
			if ((dirs[startRow, startCol] & Maze.Dir.S) == Maze.Dir.S) walkers.Add(new Walker(startCell, new Cell(startCell, Maze.Dir.S)));
			if ((dirs[startRow, startCol] & Maze.Dir.W) == Maze.Dir.W) walkers.Add(new Walker(startCell, new Cell(startCell, Maze.Dir.W)));

			// Keep looping until walker list is empty
			while (walkers.Count > 0)
			{
				// Add list of current walker cells to path.
				Cell[] cells = new Cell[walkers.Count];
				for (int wi = 0; wi < walkers.Count; wi++)
				{
					cells[wi] = new Cell(walkers[wi].CurCell);
				}
				path.Add(cells);

				// Advance each of the walkers
				List<Walker> newWalkerList = new List<Walker>();
				foreach (Walker walker in walkers)
				{
					List<Cell> nextCells = new List<Cell>();

					WalkerTest(walker, Maze.Dir.N, nextCells);
					WalkerTest(walker, Maze.Dir.E, nextCells);
					WalkerTest(walker, Maze.Dir.S, nextCells);
					WalkerTest(walker, Maze.Dir.W, nextCells);

					foreach (Cell nextCell in nextCells)
					{
						newWalkerList.Add(new Walker(walker.Cur, nextCell);
					}
				}
				walkers = newWalkerList;
			}
		}

		private static void WalkerTest(Walker walker, Maze.Dir dir, List<Cell> nextCells)
		{
			if ((dirs[w.Cur.Row, w.Cur.Col] & dir) == dir)
			{
				Cell newCell = new Cell(w.Cur, dir);
				if (!newCell.Equals(w.PrevCell))
				{
					nextCells.Add(newCell);
				}
			}
		}

		internal class Walker
		{
			public Walker(Maze.Cell curCell, Maze.Cell prevCell)
			{
				this.CurCell = curCell;
				this.PrevCell = prevCell;
			}
			public readonly Maze.Cell CurCell;
			public readonly Maze.Cell PrevCell;
		}

		internal bool RandomJoin(int row, int col)
		{
			List<Maze.Dir> dirList = new List<Maze.Dir>();

			if (row > 0 && dirs[row - 1, col] == Maze.Dir.None)
			{
				dirList.Add(Maze.Dir.N);
			}
			if (row < maxRow && dirs[row + 1, col] == Maze.Dir.None)
			{
				dirList.Add(Maze.Dir.S);
			}
			if (col > 0 && dirs[row, col - 1] == Maze.Dir.None)
			{
				dirList.Add(Maze.Dir.E);
			}
			if (col < maxCol 0 && dirs[row, col + 1] == Maze.Dir.None)
			{
				dirList.Add(Maze.Dir.W);
			}

			if (dirList.Count == 0)
			{
				return false;
			}

			Maze.Dir dir = dirList[random.Next(dirList.Count)];
			Maze.Cell nn = new Maze.Cell(row, col, dir);

			dirs[row, col] |= dir;
			dirs[nn.Row, nn.Col] |= Maze.Opposite(dir);

			return true;
		}
	}
}
