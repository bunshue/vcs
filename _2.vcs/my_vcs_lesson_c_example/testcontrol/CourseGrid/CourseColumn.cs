using System;
using System.Drawing;
using System.Windows.Forms;
using System.Data;
using System.Collections;

namespace hisonic.WinForm.HisonicControl.CourseGrid
{
	/// <summary>
	/// CourseCommonColumn 的摘要说明。
	/// 对于某种数据的特殊颜色显示支持。
	/// </summary>
	public class CourseCommonColumn : DataGridTextBoxColumn
	{
		private Color foreColor = SystemColors.WindowText;
		private Color backColor = SystemColors.Window;

		private Color selectedForeColor = SystemColors.HighlightText;
		private Color selectedBackColor = SystemColors.Highlight;

		// 是否启用状态颜色
		private bool isStateToColor = false;
		// 该列格子的状态数组
		private int[] gridState = null;
		// 状态颜色表
		// 用整数的状态值做键，取得颜色。
		private Hashtable stateBackColorTable = null;
		private Hashtable stateForeColorTable = null;
		// 本列的行数
		private int _rowCount;

		public bool IsStateToColor
		{
			set
			{
				if(gridState == null || stateBackColorTable == null || stateForeColorTable == null)
				{
					this.isStateToColor = false;
				}
				else
				{
					this.isStateToColor = value;
				}
			}
		}

		public Hashtable StateBackColorTable
		{
			set
			{
				this.stateBackColorTable = value;
			}
		}

		public Hashtable StateForeColorTable
		{
			set
			{
				this.stateForeColorTable = value;
			}
		}

		public Color ForeColor
		{
			get
			{
				return foreColor;
			}
			set
			{
				foreColor = value;
			}
		}

		public Color BackColor
		{
			get
			{
				return backColor;
			}
			set
			{
				backColor = value;
			}
		}

		public Color SelectedForeColor
		{
			get
			{
				return selectedForeColor;
			}
			set
			{
				selectedForeColor = value;
			}
		}

		public Color SelectedBackColor
		{
			get
			{
				return selectedBackColor;
			}
			set
			{
				selectedBackColor = value;
			}
		}

		/*	protected override void Edit(
				CurrencyManager source,
				int rowNum,
				Rectangle bounds,
				bool readOnly
				)
			{
				EndEdit();
			}

			protected override void Edit(
				CurrencyManager source,
				int rowNum,
				Rectangle bounds,
				bool readOnly,
				string instantText
				)
			{
				EndEdit();
			}

			protected override void Edit(
				CurrencyManager source,
				int rowNum,
				Rectangle bounds,
				bool readOnly,
				string instantText,
				bool cellIsVisible
				)
			{
				EndEdit();
			}
		*/

		protected override void Paint( Graphics g,
			Rectangle bounds,
			CurrencyManager source,
			int rowNum
			)
		{
			if(this.TextBox != null)
			{
				this.TextBox.ForeColor = this.SelectedForeColor;
				this.TextBox.BackColor = this.selectedBackColor;
			}
			base.Paint(g, bounds, source, rowNum);
		}

		protected override void Paint(Graphics g,
			Rectangle bounds,
			CurrencyManager source,
			int rowNum,
			bool alignToRight
			)
		{
			if(this.TextBox != null)
			{
				this.TextBox.ForeColor = this.SelectedForeColor;
				this.TextBox.BackColor = this.selectedBackColor;
			}
			base.Paint(g, bounds, source, rowNum, alignToRight);
		}

		protected override void Paint(Graphics g,
			Rectangle bounds,
			CurrencyManager source,
			int rowNum,
			Brush backBrush,
			Brush foreBrush,
			bool alignToRight
			)
		{
			Brush myBackBrush = (Brush) backBrush.Clone();
			Brush myForeBrush = (Brush) foreBrush.Clone();

			DataGridTableStyle gridTableStyle = this.DataGridTableStyle.DataGrid.TableStyles[0];
			string temp = 
				gridTableStyle.GridColumnStyles[this.DataGridTableStyle.DataGrid.CurrentCell.ColumnNumber].MappingName;
			if (source.Position == rowNum && temp == this.MappingName)
			{
				if (myBackBrush is SolidBrush)
				{
					// use selected brush
					((SolidBrush)myBackBrush).Color = selectedBackColor;
				}

				if (myForeBrush is SolidBrush)
				{
					// use selected brush
					((SolidBrush)myForeBrush).Color = selectedForeColor;
				}
			}
			else
			{
				if(this.isStateToColor == true)
				{
					if (myBackBrush is SolidBrush)
					{
						if(this.stateBackColorTable[this.gridState[rowNum]] != null)
						{
							Color c = (Color) this.stateBackColorTable[this.gridState[rowNum]];
							((SolidBrush)myBackBrush).Color = c;
						}
					}

					if (myForeBrush is SolidBrush)
					{						
						if(this.stateForeColorTable[this.gridState[rowNum]] != null)
						{
							Color c = (Color) this.stateForeColorTable[this.gridState[rowNum]];
							((SolidBrush)myForeBrush).Color = c;
						}
					}
				}
				else
				{
					if (myBackBrush is SolidBrush)
					{
						((SolidBrush)myBackBrush).Color = backColor;
					}

					if (myForeBrush is SolidBrush)
					{
						// use selected brush
						((SolidBrush)myForeBrush).Color = foreColor;
					}
				}				
			}

			if(this.TextBox != null)
			{
				this.TextBox.ForeColor = this.SelectedForeColor;
				this.TextBox.BackColor = this.selectedBackColor;
			}
			base.Paint(g, bounds, source, rowNum, myBackBrush, myForeBrush,
				alignToRight);
		}

		/// <summary>
		/// 生成本列单元格状态数组
		/// </summary>
		/// <param name="rowCount">课表的行数</param> 
		public void GenerateState(int rowCount)
		{
			this._rowCount = rowCount;
			this.gridState = new int[rowCount];
		}

		/// <summary>
		/// 清除状态
		/// 状态取大于0的值，0表示选中，小于0表示无效状态		/// 
		/// </summary>
		public void ClearState( )
		{
			for(int i=0;i<_rowCount;++i)
			{
				this.gridState[i] = -1;
			}
		}

		/// <summary>
		/// 设置单元格状态值
		/// </summary>
		/// <param name="rowNum">行号</param>
		/// <param name="state">状态值</param>
		public void SetGridState(int rowNum, int state)
		{
			if(rowNum<0 || rowNum>(_rowCount-1))
			{
				return;
			}
			this.gridState[rowNum] = state;
		}

		/// <summary>
		/// 获取单元格状态值
		/// </summary>
		/// <param name="rowNum">行号</param>
		/// <returns></returns>
		public int GetGridState(int rowNum)
		{
			return this.gridState[rowNum];
		}
	}
}