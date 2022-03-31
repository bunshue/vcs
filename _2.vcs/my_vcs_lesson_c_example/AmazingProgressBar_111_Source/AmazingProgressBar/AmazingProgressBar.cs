using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Diagnostics;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Data;
using System.Text;
using System.Windows.Forms;

namespace GAW
{
    /// <summary>
    /// 	AmazingProgressBar control.
    /// </summary>
    public partial class AmazingProgressBar : ProgressBar
    {
        /// <summary>
        /// 	Default constructor.
        /// </summary>
        public AmazingProgressBar()
        {
			SetStyle(  ControlStyles.AllPaintingInWmPaint
					 | ControlStyles.OptimizedDoubleBuffer
					 | ControlStyles.UserPaint, true);

			base.Style = ProgressBarStyle.Continuous;

			maze = null;
			marqueeTimer = new Timer();
            marqueeTimer.Tick += new System.EventHandler(this.MarqueeTimer_Tick);
        }

        /// <summary>
        /// 	Gets or sets the minimum value of the range of the control.
        /// </summary>
		/// <remarks>
		/// 	Refer to the .NET 2.0 documenation for <c>ProgressBar.Minimum</c> for more information.
		/// </remarks>
        /// <value>
        /// 	The minimum value of the range of the control. The default is 0.
        /// </value>
		/// <exception cref="System.ArgumentException">
		///		The value specified is less than 0.
		/// </exception>
		public new int Minimum
		{
			get { return base.Minimum; }
			set
			{
				if (base.Minimum != value)
				{
					base.Minimum = value;
					Redraw();
				}
			}
		}

        /// <summary>
        /// 	Gets or sets the maximum value of the range of the control.
        /// </summary>
		/// <remarks>
		/// 	Refer to the .NET 2.0 documenation for <c>ProgressBar.Maximum</c> for more information.
		/// </remarks>
        /// <value>
        /// 	The maximum value of the range of the control. The default is 100.
        /// </value>
		/// <exception cref="System.ArgumentException">
		///		The value specified is less than 0.
		/// </exception>
		public new int Maximum
		{
			get { return base.Maximum; }
			set
			{
				if (base.Maximum != value)
				{
					base.Maximum = value;
					Redraw();
				}
			}
		}

        /// <summary>
        /// 	Gets or sets the current position of the progress bar.
        /// </summary>
		/// <remarks>
		/// 	Refer to the .NET 2.0 documenation for <c>ProgressBar.Value</c> for more information.
		/// </remarks>
        /// <value>
        /// 	The position within the range of the property bar. The default is 0.
        /// </value>
		/// <exception cref="System.ArgumentException">
		///		The value specified is greater than the value of the <c>Maximum</c> property, or
		/// 	the value specified is less than the value of the <c>Minimum</c> property.
		/// </exception>
		public new int Value
		{
			get { return base.Value; }
			set
			{
				if (base.Value != value)
				{
					base.Value = value;
					Redraw();
				}
			}
		}

        /// <summary>
        /// 	Gets or sets the manner in which progress should be indicated on the progress bar. 
        /// </summary>
		/// <value>
		/// 	One of the ProgressBarStyle values. The default is Continous.
		/// </value>
		/// <remarks>
		/// 	Refer to the .NET 2.0 documenation for <c>ProgressBar.Style</c> for more information.
		/// </remarks>
		public new ProgressBarStyle Style
		{
			get { return base.Style; }
			set
			{
				if (base.Style != value)
				{
					base.Style = value;
					MarqueeUpdate();
					Redraw();
				}
			}
		}

        /// <summary>
        /// 	Gets or the time period, in milliseconds, that it takes the progress block to scroll across the progress bar. 
        /// </summary>
		/// <value>
		/// 	The time period, in milliseconds, that it takes the progress block to scroll across the progress bar. 
		/// </value>
		/// <exception cref="System.ArgumentOutOfRangeException">
		///		The value specified is less than one.
		/// </exception>
		public new int MarqueeAnimationSpeed
		{
			get { return base.MarqueeAnimationSpeed; }
			set
			{
				if (base.MarqueeAnimationSpeed != value)
				{
					base.MarqueeAnimationSpeed = value;
					MarqueeUpdate();
					Redraw();
				}
			}
		}

		private int rowCount = 3;
		/// <summary>
		/// 	Gets or sets the number of rows in the maze.
		/// </summary>
		/// <value>
		/// 	The number of rows in the maze.
		/// </value>
		/// <remarks>
		/// 	The size and complexity of the maze generally depends on the this parameter.
		/// 	A value of 1 results in a maze which looks just like a standard progress bar.
		/// 	A value of 2 results in a distinctly uninteresting maze.
		/// 	A value of 3 or more is strongly recommended.
		/// </remarks>
		/// <exception cref="System.ArgumentOutOfRangeException">
		///		The value specified is less than one.
		/// </exception>
		public int RowCount
		{
			get { return rowCount; }
			set 
			{
				if (value != rowCount)
				{
					if (value < 1)
					{
						throw new ArgumentOutOfRangeException("RowCount");
					}
					rowCount = value;
					Regenerate();
				}
			}
		}

		private int colCount = 0;
		/// <summary>
		/// 	Gets the number of columns in the maze.
		/// </summary>
		/// <value>
		///		The number of columns in the maze.
		///		<para>
		///		This value is determined internally by the class
		/// 	as the largest possible value given the size of the control,
		///		and the current values of <c>RowCount</c>, <c>WallSize</c> and <c>BorderSize</c>.
		///		</para>
		/// </value>
		public int ColCount
		{
			get { return colCount; }
		}

        /// <summary>
		/// 	Gets the number of cells in the maze.
		/// </summary>
		/// <value>
		///		The number of cells in the maze.
		///		Equivalent to <c>RowCount</c> times <c>ColCount</c>.
		/// </value>
		public int CellCount
		{
			get { return rowCount * colCount; }
		}

		private int cellSize = 0;
		/// <summary>
		/// 	Gets the pixel size of a cell in the maze.
		/// </summary>
		/// <value>
		///		The height and width of each maze cell.
		///		<para>
		///		This value is determined internally by the class given the size of the control,
		///		and the current values of <c>RowCount</c>, <c>ColCount</c>, <c>WallSize</c> and <c>BorderSize</c>.
		///		</para>
		/// </value>
		public int CellSize
		{
			get { return cellSize; }
		}

		/// <summary>
		/// 	Gets the length of the longest path in the maze.
		/// </summary>
		/// <value>
		/// 	The length of the longest path in the maze.
		/// 	This value will be less than or equal to <c>CellCount</c>.
		/// 	If the maze has but a single path with no branching, this value will be equal to <c>CellCount</c>.
		///	</value>
		public int PathLength
		{
			get
			{
				if (maze == null)
				{
					return 0;
				}
				return maze.Paths.GetLength(0);
			}
		}

        /// <summary>
        /// 	The style and general direction of the maze.
        /// </summary>
        /// <remarks>
		/// 	The generated mazes do not have loops, and branching is avoided
		/// 	(though a small amount may occur if <c>RowCount</c> is greater than 3).
		///		The maze directions are the general directions, though
		/// 	there will be always be twists and turns and some doubling back.
        /// </remarks>
		public enum MazeStyleType
		{
		    /// <summary>
			/// 	A maze with a single path going left to right.
		    /// </summary>
		    SingleRight,
		    
		    /// <summary>
		    /// 	A maze with a single path going left to right.
		    /// </summary>
		    SingleLeft,
		    
		    /// <summary>
		    /// 	A maze with a single path going bottom to top.
		    /// </summary>
		    SingleUp,
		    
		    /// <summary>
		    /// 	A maze with a single path going top to bottom.
		    /// </summary>
		    SingleDown,

			/// <summary>
			/// 	A maze in which paths start at the right and left ends, converging in the middle.
			/// </summary>
			SplitConvergeHorizontal,
			
			/// <summary>
			/// 	A maze in which paths start at the top and bottom, converging in the middle.
			/// </summary>
			SplitConvergeVertical,
			
			/// <summary>
			/// 	A maze in which paths start in the middle, ending at the right and left ends.
			/// </summary>
			SplitDivergeHorizontal,
			
			/// <summary>
			/// 	A maze in which paths start in the middle, ending at the top and bottom.
			/// </summary>
			SplitDivergeVertical
		};

		private MazeStyleType mazeStyle = MazeStyleType.SingleRight;
		/// <summary>
		/// 	Gets or sets the maze style.
		/// </summary>
		/// <value>
		/// 	The <c>AmazingProgressBar.MazeStyleType</c> value indicating the style and general direction of the maze.
		/// </value>
		public MazeStyleType MazeStyle
		{
			get { return mazeStyle; }
			set
			{
				if (value != mazeStyle)
				{
					mazeStyle = value;
					Regenerate();
				}
			}
		}

		/// <summary>
		/// 	Coloring of filled cells.
		/// </summary>
		public enum GradientType
		{
		    /// <summary>
		    /// 	No gradient coloring.  All filled cells are <c>ForeColor</c>
		    /// </summary>
		    None,
		    
		    /// <summary>
		    /// 	Each row in the maze is a different color, spanning a gradient with
			/// 	the first row being <c>GradientStartColor</c>, and the last row being <c>GradientEndColor</c>.
		    /// </summary>
		    Rows,
		    
		    /// <summary>
		    /// 	Each column in the maze is a different color, spanning a gradient with
			/// 	the first column being <c>GradientStartColor</c>, and the last column being <c>GradientEndColor</c>.
		    /// </summary>
		    Columns,
		    
		    /// <summary>
		    /// 	Each cell in the maze is a different color, spanning a gradient with
			/// 	the first cell being <c>GradientStartColor</c>, and the last cell being <c>GradientEndColor</c>.
		    /// </summary>
		    Flow
        };

		private GradientType gradient;
		/// <summary>
		/// 	Gets or sets the gradient type.
		/// </summary>
		/// <value>
		/// 	The <c>AmazingProgressBar.GradientType</c> value indicating the type of gradient used for coloring filled cells.
		/// </value>
		public GradientType Gradient
		{
			get { return gradient; }
			set
			{
				if (value != gradient)
				{
					gradient = value;
					gradientColors = null;
					Redraw();
				}
			}
		}

		private Color gradientStartColor = Color.PaleGreen;
		/// <summary>
		/// 	Gets or set the start gradient color.
		/// </summary>
		/// <value>
		/// 	The start color of the gradient.
		/// 	Only used if <c>Gradient</c> is not <c>AmazingProgressBar.GradientType.None</c>.
		/// </value>
		[Category("Appearance"), DefaultValue("PaleGreen")]
		public Color GradientStartColor
		{
			get { return gradientStartColor; }
			set
			{
				if (gradientStartColor.ToArgb() != value.ToArgb())
				{
					gradientStartColor = value;
					gradientColors = null;
					Redraw();
				}
			}
		}

		private Color gradientEndColor = Color.Lime;
		/// <summary>
		/// 	Gets or set the end gradient color.
		/// </summary>
		/// <value>
		/// 	The end color of the gradient.
		/// 	Only used if <c>Gradient</c> is not <c>AmazingProgressBar.GradientType.None</c>.
		/// </value>
		[Category("Appearance"), DefaultValue("PaleGreen")]
		public Color GradientEndColor
		{
			get { return gradientEndColor; }
			set
			{
				if (gradientEndColor.ToArgb() != value.ToArgb())
				{
					gradientEndColor = value;
					gradientColors = null;
					Redraw();
				}
			}
		}

		private int wallSize = 1;
		/// <summary>
		/// 	Gets or sets the size of the maze walls.
		/// </summary>
		/// <value>
		/// 	The size of the maze walls in pixels.
		/// </value>
		///	<remarks>
		/// 	Combine a wall size of zero and a <c>Style</c> of <c>ProgressBarStyle.Blocks</c> for an
		/// 	interesting visual effect.
		///	</remarks>
		public int WallSize
		{
			get { return wallSize; }
			set
			{
				int v = Math.Max(0, value);
				if (wallSize != v)
				{
					wallSize = v;
					Regenerate();
				}
			}
		}

		private Color wallColor = Color.Black;
		/// <summary>
		/// 	Gets or set the color of the maze walls.
		/// </summary>
		/// <value>
		/// 	The color of the maze walls.
		/// </value>
		///	<remarks>
		/// 	Set the maze wall color to <c>BackColor</c> for an interesting visual effect.
		///	</remarks>
		[Category("Appearance"), DefaultValue("Black")]
		public Color WallColor
		{
			get { return wallColor; }
			set
			{
				if (wallColor.ToArgb() != value.ToArgb())
				{
					wallColor = value;
					Redraw();
				}
			}
		}

		private int borderSize = 0;
		/// <summary>
		/// 	Gets or sets the size of the maze border.
		/// </summary>
		/// <value>
		/// 	The size of the maze border in pixels.
		/// 	The border is drawn around the outside of the maze.
		/// </value>
		public int BorderSize
		{
			get { return borderSize; }
			set
			{
				int v = Math.Max(0, value);
				if (borderSize != v)
				{
					borderSize = v;
					borderColors = null;
					Regenerate();
				}
			}
		}

		private Color borderColor = Color.Black;
		/// <summary>
		/// 	Gets or sets the color of the maze border.
		/// </summary>
		/// <value>
		/// 	The color of the border.  The border is drawn around the outside of the maze.
		/// </value>
		[Category("Appearance"), DefaultValue("Black")]
		public Color BorderColor
		{
			get { return borderColor; }
			set
			{
				if (borderColor.ToArgb() != value.ToArgb())
				{
					borderColor = value;
					borderColors = null;
					Redraw();
				}
			}
		}

		private bool borderGradient = false;
		/// <summary>
		/// 	Gets or sets whether the border is drawn as a gradient.
		/// </summary>
		/// <value>
		/// 	<c>True</c> if the border is drawn as a gradient, <c>false</c> otherwise.
		/// 	<para>
		/// 	If <c>true</c>, the border color is a gradient from <c>BorderColor</c>
		/// 	to <c>UnusedColor</c>.
		/// 	If <c>false</c>, the entire border is <c>BorderColor</c>.
		///     </para>
		/// </value>
		public bool BorderGradient
		{
			get { return borderGradient; }
			set
			{
				if (borderGradient != value)
				{
					borderGradient = value;
					borderColors = null;
					Redraw();
				}
			}
		}


		private bool borderRoundCorners = false;
		/// <summary>
		/// 	Gets or sets whether the border is drawn with round corners.
		/// </summary>
		/// <value>
		/// 	<c>True</c> if the border is drawn with round borders, <c>false</c> otherwise.
		/// </value>
		public bool BorderRoundCorners
		{
			get { return borderRoundCorners; }
			set
			{
				if (borderRoundCorners != value)
				{
					borderRoundCorners = value;
					Redraw();
				}
			}
		}


		private Color unusedColor = SystemColors.Control;
		/// <summary>
		/// 	Gets or sets the color of the unused area of the control.
		/// </summary>
		/// <value>
		/// 	The color of the unused area of the control.
		/// 	Should be left as <c>SystemColors.Control</c>.
		/// </value>
		[Category("Appearance"), DefaultValue("Control")]
		public Color UnusedColor
		{
			get { return unusedColor; }
			set
			{
				if (unusedColor.ToArgb() != value.ToArgb())
				{
					unusedColor = value;
					Redraw();
				}
			}
		}

		/// <summary>
		/// 	Represents the method that is called when the maze layout changes.
		/// </summary>
		/// <remarks>
		/// 	The maze layout may change whenever any of the following changes:
		/// 	the size of the control, <c>RowCount</c>, <c>WallSize</c>, <c>BorderSize</c>, or <c>MazeStyle</c>.
		/// 	It will also change if <c>Regenerate</c> is called.
		/// 	But a new maze is not actually generated until painting occurs.
		/// 	This method is called immediately after a new maze is generated, but
		/// 	before it is displayed.
		/// </remarks>
		public event EventHandler MazeChanged = null;

        /// <summary>
        /// 	Generate a new maze.
        /// </summary>
		public void Regenerate()
		{
			maze = null;
			Redraw();
		}

        private void Redraw()
        {
			Invalidate(true);
        }

		private void MazeCannotFit(PaintEventArgs e)
		{
			Size cs = ClientSize;

			Brush br = new SolidBrush(Color.LightGray);
			e.Graphics.FillRectangle(br, 0, 0, cs.Width, cs.Height);
			br.Dispose();

			br = new HatchBrush(HatchStyle.Wave, Color.Pink);
			e.Graphics.FillRectangle(br, 0, 0, cs.Width, cs.Height);
			br.Dispose();
		}

		private void MarqueeUpdate()
		{
			if (base.Style == ProgressBarStyle.Marquee && maze != null)
			{
				marqueeLength = Math.Max(PathLength / 6, 1);
				marqueePosition = -marqueeLength;
				marqueeTimer.Interval = Math.Max(MarqueeAnimationSpeed / PathLength, 5);
				marqueeTimer.Enabled = true;
			}
			else
			{
				marqueeTimer.Enabled = false;
			}
		}

		private void MarqueeTimer_Tick(object sender, EventArgs e)
		{
			marqueePosition++;
			if (marqueePosition - marqueeLength >= PathLength)
			{
				marqueePosition = -marqueeLength;
			}
			Redraw();
		}

		private Maze maze = null;

		private Timer marqueeTimer = null;
		private int marqueePosition = 0;
		private int marqueeLength = 0;

		private Color[] gradientColors = null;
		private Color[] borderColors = null;

		private int rowPixels;
		private int unusedRowPixels;
		private int unusedTopPixels;
		private int unusedBottomPixels;

		private int colPixels;
		private int unusedColPixels;
		private int unusedLeftPixels;
		private int unusedRightPixels;

		private int innerWidth;
		private int innerHeight;

		private Graphics g;

        /// <summary>
        ///     Called when paint event is raised.
        /// </summary>
        /// <param name="e">Painting parameters.</param>
		protected override void OnPaint(PaintEventArgs e)
        {
			g = e.Graphics;

			// Is there enough space for maze rows?
			rowPixels = this.ClientSize.Height;
			colPixels = this.ClientSize.Width;
			int borderPixels = 2 * borderSize;

			int rowCellPixels = rowPixels - (rowCount + 1) * wallSize - borderPixels;
			cellSize = rowCellPixels / rowCount;
			if (cellSize < 1)
			{
				MazeCannotFit(e);
				return;
			}

			// How many column cells?
			int colCellPixels = colPixels - wallSize - borderPixels;
			int newColCount = colCellPixels / (cellSize + wallSize);
			if (newColCount < 1)
			{
				MazeCannotFit(e);
				return;
			}

			// Need to regen maze?
			if (colCount != newColCount)
			{
				maze = null;
			}
			colCount = newColCount;
			if (maze == null)
			{
				switch (mazeStyle)
				{
					case MazeStyleType.SingleRight       : maze = MazeSinglePath.Generate(rowCount, colCount, Maze.Dir.E); break;
					case MazeStyleType.SingleLeft        : maze = MazeSinglePath.Generate(rowCount, colCount, Maze.Dir.W); break;
					case MazeStyleType.SingleUp          : maze = MazeSinglePath.Generate(rowCount, colCount, Maze.Dir.N); break;
					case MazeStyleType.SingleDown        : maze = MazeSinglePath.Generate(rowCount, colCount, Maze.Dir.S); break;

					case MazeStyleType.SplitConvergeHorizontal : maze = MazeSplitPath.Generate(rowCount, colCount, MazeSplitPath.PathType.ConvergeEW); break;
					case MazeStyleType.SplitConvergeVertical   : maze = MazeSplitPath.Generate(rowCount, colCount, MazeSplitPath.PathType.ConvergeNS); break;
					case MazeStyleType.SplitDivergeHorizontal  : maze = MazeSplitPath.Generate(rowCount, colCount, MazeSplitPath.PathType.DivergeEW);  break;
					case MazeStyleType.SplitDivergeVertical    : maze = MazeSplitPath.Generate(rowCount, colCount, MazeSplitPath.PathType.DivergeNS);  break;
				}
				if (MazeChanged != null)
				{
					MazeChanged(this, null);
				}
				gradientColors = null;
				MarqueeUpdate();
			}

			// All cells are square - so might have "unused" pixels left over
            unusedRowPixels = rowPixels - (rowCount * cellSize) - ((rowCount + 1) * wallSize) - borderPixels;
			unusedTopPixels = unusedRowPixels / 2;
			unusedBottomPixels = unusedRowPixels - unusedTopPixels;

            unusedColPixels = colPixels - (colCount * cellSize) - ((colCount + 1) * wallSize) - borderPixels;
			unusedLeftPixels = unusedColPixels / 2;
			unusedRightPixels = unusedColPixels - unusedLeftPixels;

			innerWidth = colPixels - unusedColPixels - borderPixels;
			innerHeight = rowPixels - unusedRowPixels - borderPixels;

			// 1. Fill with unused color
			Brush br = new SolidBrush(unusedColor);
			g.FillRectangle(br, 0, 0, this.ClientSize.Width, this.ClientSize.Height);
			br.Dispose();

			// 2. Fill inside with background color
			br = new SolidBrush(base.BackColor);
			g.FillRectangle(br, unusedLeftPixels + borderSize,
    							unusedTopPixels + borderSize,
	    						colPixels - unusedColPixels - borderPixels,
		    					rowPixels - unusedRowPixels - borderPixels);
			br.Dispose();

			// 3. Fill cells
			FillCells();

			// 4. Draw walls
			DrawWalls();

			// 5. Draw borders
			DrawBorder();
		}

		private void DrawBorder()
		{
			if (borderSize <= 0)
			{
				return;
			}

			GenerateBorderColors();

			// Draw borders inside to out
			int x = unusedLeftPixels + borderSize - 1;
			int width = colPixels - unusedColPixels - 2 * borderSize + 1;
			int y = unusedTopPixels + borderSize - 1;
			int height = rowPixels - unusedRowPixels - 2 * borderSize + 1;

			int bf = (borderSize > 1 && borderRoundCorners) ? (borderSize - 1) : 0;

			for (int i = 0; i < borderSize; i++)
			{
				Pen pen = new Pen(borderColors[i]);
				if (borderRoundCorners)
				{
					g.DrawLine(pen, x,              y + i + bf + 1,  x,                      y + height - i - bf - 1);
					g.DrawLine(pen, x + width,      y + i + bf + 1,  x + width,              y + height - i - bf - 1);
					g.DrawLine(pen, x + i + bf + 1, y,               x + width - i - bf - 1, y);
					g.DrawLine(pen, x + i + bf + 1, y + height,      x + width - i - bf - 1, y + height);

					Pen arcPen = new Pen(borderColors[i], (i == 0 || i == (borderSize - 1)) ? 1.0f : 2.0f);

					int size = 2 * (i + bf + 1);
					g.DrawArc(arcPen, x, y, size, size, 180, 90);
					g.DrawArc(arcPen, x, y + height - size, size, size, 90, 90);
					g.DrawArc(arcPen, x + width - size, y, size, size, 270, 90);
					g.DrawArc(arcPen, x + width - size, y + height - size, size, size, 0, 90);
					arcPen.Dispose();
				}
				else
				{
					g.DrawRectangle(pen, x, y, width, height);
				}
				pen.Dispose();
 				x--; width += 2;
				y--; height += 2;
			}
		}

		private void GenerateBorderColors()
		{
			if (borderColors != null || borderSize == 0)
			{
				return;
			}

			borderColors = new Color[borderSize];
			borderColors[0] = borderColor;

			if (borderSize > 1)
			{
				float dA = borderGradient ? (float)(unusedColor.A - borderColor.A) / (float)borderSize : 0.0f;
				float dR = borderGradient ? (float)(unusedColor.R - borderColor.R) / (float)borderSize : 0.0f;
				float dG = borderGradient ? (float)(unusedColor.G - borderColor.G) / (float)borderSize : 0.0f;
				float dB = borderGradient ? (float)(unusedColor.B - borderColor.B) / (float)borderSize : 0.0f;

				for (int i = 1; i < borderSize; i++)
				{
					borderColors[i] = Color.FromArgb((int)((float)borderColor.A + dA * (float)i),
													 (int)((float)borderColor.R + dR * (float)i),
													 (int)((float)borderColor.G + dG * (float)i),
													 (int)((float)borderColor.B + dB * (float)i));

				}
			}
		}

		private void GenerateGradientColors()
		{
			if (gradientColors != null || gradient == GradientType.None)
			{
				return;
			}

			int gradCount = 0;
			switch (gradient)
			{
				case GradientType.Rows    : gradCount = RowCount;   break;
				case GradientType.Columns : gradCount = ColCount;   break;
				case GradientType.Flow    : gradCount = PathLength; break;
			}

			gradientColors = new Color[gradCount];

			gradientColors[0] = gradientStartColor;
			gradientColors[gradCount - 1] = gradientEndColor;

			if (gradCount > 2)
			{
				float dA = (float)(gradientEndColor.A - gradientStartColor.A) / (float)(gradCount - 1);
				float dR = (float)(gradientEndColor.R - gradientStartColor.R) / (float)(gradCount - 1);
				float dG = (float)(gradientEndColor.G - gradientStartColor.G) / (float)(gradCount - 1);
				float dB = (float)(gradientEndColor.B - gradientStartColor.B) / (float)(gradCount - 1);

				for (int i = 1; i < (gradCount - 1); i++)
				{
					gradientColors[i] = Color.FromArgb((int)((float)gradientStartColor.A + dA * (float)i),
													   (int)((float)gradientStartColor.R + dR * (float)i),
													   (int)((float)gradientStartColor.G + dG * (float)i),
													   (int)((float)gradientStartColor.B + dB * (float)i));
				}
			}
		}

		private void FillCells()
		{
            if (Maximum <= Minimum || Value < Minimum) // sanity checks
            {
                return;
            }

			int startIndex = 0;
			int endIndex = 0;

			if (base.Style == ProgressBarStyle.Marquee)
			{
				startIndex = Math.Max(0, marqueePosition - marqueeLength);
				endIndex = Math.Min(PathLength - 1, marqueePosition + marqueeLength);
			}
			else
			{
				// How many cells to fill?
				float cellsPerStep = (float)PathLength / (float)(Maximum - Minimum);
				int filledCells = (int)Math.Floor(cellsPerStep * (Value - Minimum));
				if (filledCells == 0)
				{
					return;
				}
	            if (Value >= Maximum) // another sanity check
	            {
	                filledCells = PathLength;
	            }
				endIndex = filledCells - 1;
			}
			FillCells(startIndex, endIndex);
		}

		private void FillCells(int startIndex, int endIndex)
		{
			GenerateGradientColors();

			int cellWidening = 0;
			int cellOffset = 0;
			if (   base.Style == ProgressBarStyle.Continuous
				|| base.Style == ProgressBarStyle.Marquee)
			{
				cellWidening = (wallSize + 1) / 2;
			}
			else if (cellSize > 2)
			{
				cellOffset = 0;
				cellWidening = -1;
			}
			int cellFullSize = cellSize + 2 * cellWidening;

			Brush br = new SolidBrush(ForeColor);

			int skip = cellSize + wallSize;

			int colConst = unusedLeftPixels + borderSize + wallSize - cellWidening + cellOffset;
			int rowConst = unusedTopPixels  + borderSize + wallSize - cellWidening + cellOffset;

			for (int ci = startIndex; ci <= endIndex; ci++)
			{
				Maze.Cell[] cells = maze.Paths[ci];

                foreach (Maze.Cell cell in cells)
                {
					if (gradient != GradientType.None)
					{
						Color color = Color.Empty;
						switch (gradient)
						{
							case GradientType.Rows    : color = gradientColors[cell.Row]; break;
							case GradientType.Columns : color = gradientColors[cell.Col]; break;
							case GradientType.Flow    : color = gradientColors[ci];       break;
						}
						br.Dispose();
						br = new SolidBrush(color);
					}

                    int x = colConst + cell.Col * skip;
                    int y = rowConst + cell.Row * skip;
                    g.FillRectangle(br, x, y, cellFullSize, cellFullSize);
                }
			}

			br.Dispose();
		}


		private void DrawWalls()
		{
			if (wallSize < 1)
			{
				return;
			}

			Brush br = new SolidBrush(wallColor);

			int edgeWidth = colCount * (cellSize + wallSize) + wallSize;
			int edgeHeight = rowCount * (cellSize + wallSize) + wallSize;

			// Draw north-most wall
			g.FillRectangle(br, unusedLeftPixels + borderSize,
    							unusedTopPixels + borderSize,
	    						edgeWidth,
		    					wallSize);

			// Draw south-most wall
			g.FillRectangle(br, unusedLeftPixels + borderSize,
    							rowPixels - unusedBottomPixels - borderSize - wallSize,
	    						edgeWidth,
		    					wallSize);

			// Draw west-most wall
			g.FillRectangle(br, unusedLeftPixels + borderSize,
    							unusedTopPixels + borderSize,
	    						wallSize,
		    					edgeHeight);

			// Draw east-most wall
			g.FillRectangle(br, colPixels - unusedRightPixels - borderSize - wallSize,
    							unusedTopPixels + borderSize,
	    						wallSize,
		    					edgeHeight);

			// Draw south walls (except for last row)
			int y = unusedTopPixels + borderSize + wallSize + cellSize;
			int dx = wallSize + cellSize + wallSize;
			int dy = wallSize;
			int skip = cellSize + wallSize;
			for (int r = 0; r < rowCount - 1; r++)
			{
				int x = unusedLeftPixels + borderSize;
				for (int c = 0; c < colCount; c++)
				{
                    if ((maze.Map[r, c] & Maze.Dir.S) != Maze.Dir.S)
					{
						g.FillRectangle(br, x, y, dx, dy);
					}
					x += skip;
				}
				y += skip;
			}

			// Draw east walls (except for last col)
			y = unusedTopPixels + borderSize;
			dx = wallSize;
			dy = wallSize + cellSize + wallSize;
			for (int r = 0; r < rowCount; r++)
			{
				int x = unusedLeftPixels + borderSize + wallSize + cellSize;
				for (int c = 0; c < colCount - 1; c++)
				{
                    if ((maze.Map[r, c] & Maze.Dir.E) != Maze.Dir.E)
					{
						g.FillRectangle(br, x, y, dx, dy);
					}
					x += skip;
				}
				y += skip;
			}

			br.Dispose();
		}
	}
}
